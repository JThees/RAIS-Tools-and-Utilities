import os
import tempfile
import webbrowser
import re
from pathlib import Path
from flask import Flask, render_template, request, send_file, jsonify
import pypandoc
from xhtml2pdf import pisa

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max file size

# Supported file formats (PDF can only be OUTPUT, not input)
SUPPORTED_INPUT = {'.md', '.txt', '.docx', '.html', '.odt', '.rtf'}
SUPPORTED_OUTPUT = {'.md', '.txt', '.pdf', '.docx', '.html'}

# Map file extensions to pypandoc input format names
INPUT_FORMAT_MAPPING = {
    '.md': 'markdown',
    '.txt': 'markdown',  # Plain text treated as markdown (no 'plain' input format in pandoc)
    '.docx': 'docx',
    '.html': 'html',
    '.odt': 'odt',
    '.rtf': 'rtf'
}

# Map user-friendly output format names to pypandoc format names
OUTPUT_FORMAT_MAPPING = {
    'md': 'markdown',
    'txt': 'plain',
    'pdf': 'pdf',
    'docx': 'docx',
    'html': 'html5'
}

def get_downloads_folder():
    """Get the user's Downloads folder path"""
    return str(Path.home() / "Downloads")

def clean_html_for_pdf(html_content):
    """Remove problematic CSS that xhtml2pdf can't handle"""
    # Remove <style> tags and their contents (xhtml2pdf has limited CSS support)
    html_content = re.sub(r'<style[^>]*>.*?</style>', '', html_content, flags=re.DOTALL)

    # Remove inline style attributes that might cause issues
    html_content = re.sub(r'\s+style="[^"]*"', '', html_content)

    # Wrap in basic HTML if not already wrapped
    if '<html' not in html_content.lower():
        html_content = f'''
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                body {{ font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }}
                h1 {{ color: #333; }}
                h2 {{ color: #666; }}
                pre {{ background: #f4f4f4; padding: 10px; }}
                code {{ background: #f4f4f4; padding: 2px 5px; }}
            </style>
        </head>
        <body>{html_content}</body>
        </html>
        '''

    return html_content

def html_to_pdf(html_content, output_path):
    """Convert HTML content to PDF using xhtml2pdf"""
    try:
        # Clean HTML to remove problematic CSS
        cleaned_html = clean_html_for_pdf(html_content)

        with open(output_path, 'wb') as pdf_file:
            pisa_status = pisa.CreatePDF(cleaned_html, dest=pdf_file)
            if pisa_status.err:
                raise Exception("PDF generation returned errors")
            return True
    except Exception as e:
        raise Exception(f"PDF generation failed: {str(e)}")

def ensure_pandoc():
    """Ensure Pandoc is installed via pypandoc"""
    try:
        pypandoc.get_pandoc_version()
    except OSError:
        print("Downloading Pandoc binaries...")
        pypandoc.download_pandoc()

@app.route('/')
def index():
    """Serve the main interface"""
    return render_template('index.html')

@app.route('/service-worker.js')
def service_worker():
    """Serve the service worker file"""
    return send_file('static/service-worker.js', mimetype='application/javascript')

@app.route('/convert', methods=['POST'])
def convert():
    """Handle file conversion"""
    try:
        # Check if file was uploaded
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400

        # Get conversion parameters
        output_format = request.form.get('output_format', 'pdf')
        action = request.form.get('action', 'download')  # 'download' or 'open'

        # Validate input file extension
        input_ext = os.path.splitext(file.filename)[1].lower()
        if input_ext not in SUPPORTED_INPUT:
            return jsonify({'error': f'Unsupported input format: {input_ext}'}), 400

        # Validate output format
        output_ext = f'.{output_format}'
        if output_ext not in SUPPORTED_OUTPUT:
            return jsonify({'error': f'Unsupported output format: {output_format}'}), 400

        # Create temporary directory for processing
        with tempfile.TemporaryDirectory() as temp_dir:
            # Save uploaded file
            input_path = os.path.join(temp_dir, file.filename)
            file.save(input_path)

            # Generate output filename
            base_name = os.path.splitext(file.filename)[0]
            output_filename = f"{base_name}{output_ext}"

            # Convert file using pypandoc
            try:
                # Both actions save to Downloads folder (so file persists for 'open')
                output_path = os.path.join(get_downloads_folder(), output_filename)

                # Get the correct pypandoc format names
                input_format = INPUT_FORMAT_MAPPING.get(input_ext)
                if not input_format:
                    return jsonify({'error': f'Invalid input format mapping for: {input_ext}'}), 400

                output_pandoc_format = OUTPUT_FORMAT_MAPPING.get(output_format)
                if not output_pandoc_format:
                    return jsonify({'error': f'Invalid output format mapping for: {output_format}'}), 400

                # Handle PDF output separately (two-step process)
                if output_format == 'pdf':
                    try:
                        # Step 1: Convert to HTML using pypandoc (no fancy CSS)
                        html_content = pypandoc.convert_file(
                            input_path,
                            'html',
                            format=input_format
                        )

                        # Step 2: Convert HTML to PDF using xhtml2pdf
                        # (CSS will be stripped/simplified automatically)
                        html_to_pdf(html_content, output_path)

                    except Exception as e:
                        error_msg = f"PDF conversion failed: {str(e)}"
                        return jsonify({'error': error_msg}), 500
                else:
                    # Non-PDF conversion - direct pypandoc
                    try:
                        pypandoc.convert_file(
                            input_path,
                            output_pandoc_format,
                            format=input_format,
                            outputfile=output_path
                        )
                    except Exception as e:
                        error_msg = f"Conversion failed: {str(e)}"
                        return jsonify({'error': error_msg}), 500

                # Handle based on action type
                if action == 'open':
                    # Open the file with default application from Downloads folder
                    webbrowser.open(output_path)
                    return jsonify({
                        'success': True,
                        'message': f'File converted and opened: {output_filename}'
                    })
                else:
                    # Return file for download
                    return send_file(
                        output_path,
                        as_attachment=True,
                        download_name=output_filename
                    )

            except Exception as e:
                return jsonify({'error': f'Conversion failed: {str(e)}'}), 500

    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    try:
        version = pypandoc.get_pandoc_version()
        return jsonify({
            'status': 'healthy',
            'pandoc_version': version
        })
    except Exception as e:
        return jsonify({
            'status': 'unhealthy',
            'error': str(e)
        }), 500

if __name__ == '__main__':
    # Ensure Pandoc is installed
    ensure_pandoc()

    # Run Flask app
    print("Starting RAIS Document Converter on http://localhost:5000")
    print("Press Ctrl+C to stop the server")
    app.run(debug=True, host='localhost', port=5000)
