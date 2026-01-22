# RAIS Document Converter

A sleek, cyberpunk-themed local web application for converting documents between multiple formats. Built for internal RAIS team use. Now available as a Progressive Web App (PWA) installable on all platforms.

## Features

- **Progressive Web App**: Installable on Windows, macOS, Linux, iOS, and Android
- **Offline Capable**: Service worker caches UI for instant loading
- **Modern Dark Interface**: Cyberpunk-inspired design with RAIS branding (black, red, gold)
- **Drag & Drop**: Intuitive file upload with visual feedback
- **Multiple Formats**: Input: MD, TXT, DOCX, HTML, ODT, RTF | Output: MD, TXT, PDF, DOCX, HTML
- **Dual Actions**:
  - **Convert & Download**: Save converted files to your Downloads folder
  - **Convert & Open**: Convert and immediately open in default application
- **Real-time Status**: Live conversion feedback with visual indicators
- **Local Processing**: All conversions happen on your machine - no cloud services

## Supported Conversions

### Input Formats
- Markdown (`.md`)
- Plain Text (`.txt`)
- Word Document (`.docx`)
- HTML (`.html`)
- OpenDocument Text (`.odt`)
- Rich Text Format (`.rtf`)

**Note**: PDF can only be used as an OUTPUT format, not input (Pandoc limitation)

### Output Formats
- Markdown (`.md`)
- Plain Text (`.txt`)
- PDF (`.pdf`)
- Word Document (`.docx`)
- HTML (`.html`)

## Quick Start

### Automated Installation

**Windows:**
```cmd
WinInstall.bat
WinRun.bat
```

**macOS:**
```bash
chmod +x MacInstall.sh MacRun.sh
./MacInstall.sh
./MacRun.sh
```

**Arch Linux:**
```bash
chmod +x ArchInstall.sh ArchRun.sh
./ArchInstall.sh
./ArchRun.sh
```

The installation scripts will:
1. Verify Python 3.8+ is installed
2. Install all required dependencies (Flask, pypandoc, xhtml2pdf, Pillow)
3. Generate PWA icons from the RAIS logo
4. Prepare the application for use

### Manual Installation

#### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

#### Setup Steps

1. **Clone or download this repository**
   ```bash
   cd raix-file-converter
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   This will install:
   - Flask (web framework)
   - pypandoc (document conversion library)
   - xhtml2pdf (PDF conversion)
   - Pillow (icon generation)

   **Note**: pypandoc will automatically download Pandoc binaries on first run.

3. **Generate PWA icons**
   ```bash
   python generate-icons.py
   ```

4. **Start the server**
   ```bash
   python app.py
   ```

## Progressive Web App Installation

The RAIS Document Converter can be installed as a standalone application on any platform.

### Desktop Installation (Windows, macOS, Linux)

1. Start the server using the run script for your platform
2. Open Chrome, Edge, or Brave browser
3. Navigate to `http://localhost:5000`
4. Click the install icon in the address bar (plus symbol or computer icon)
5. Click "Install" in the popup dialog

The application will now open in a standalone window without browser chrome.

### Mobile Installation (iOS, Android)

For detailed mobile installation instructions, including network configuration, see `PWA-INSTALL-GUIDE.md`.

**Quick overview:**
- **iOS**: Safari → Share button → "Add to Home Screen"
- **Android**: Chrome → Menu → "Install app" or "Add to Home Screen"

### Verifying PWA Installation

1. Open Developer Tools (F12)
2. Navigate to Application tab
3. Check Service Workers section - should show `service-worker.js` as activated
4. Check Manifest section - should display RAIS branding and all icon sizes

## Usage

### Starting the Server

**Automated (recommended):**
- Windows: Run `WinRun.bat`
- macOS: Run `./MacRun.sh`
- Linux: Run `./ArchRun.sh`

**Manual:**
```bash
python app.py
```

The server will start on `http://localhost:5000`

### Converting Documents

1. **Upload File**
   - Drag and drop a file onto the upload zone, OR
   - Click the upload zone to browse for a file

2. **Select Output Format**
   - Choose your desired output format using the radio buttons
   - Default is PDF

3. **Convert**
   - **Convert & Download**: Saves the converted file to your Downloads folder
   - **Convert & Open**: Converts the file and opens it with your default application

4. **Status Updates**
   - Watch the status bar at the bottom for real-time feedback
   - Success messages appear in gold
   - Errors appear in red

### File Size Limit

- Maximum file size: **50MB**
- Files larger than 50MB will be rejected with a warning

## Project Structure

```
raix-file-converter/
├── app.py                      # Flask backend server
├── requirements.txt            # Python dependencies
├── generate-icons.py           # PWA icon generator
├── WinInstall.bat             # Windows installation script
├── WinRun.bat                 # Windows run script
├── MacInstall.sh              # macOS installation script
├── MacRun.sh                  # macOS run script
├── ArchInstall.sh             # Arch Linux installation script
├── ArchRun.sh                 # Arch Linux run script
├── CLAUDE.md                  # Build instructions
├── README.md                  # This file
├── PWA-INSTALL-GUIDE.md       # Detailed PWA installation guide
├── README-PWA.md              # PWA feature documentation
├── static/
│   ├── logo.png               # RAIS hexagon logo
│   ├── style.css              # Cyberpunk dark theme styles
│   ├── manifest.json          # PWA manifest
│   ├── service-worker.js      # PWA service worker
│   └── icons/                 # PWA icons (8 sizes: 72px-512px)
│       ├── icon-72x72.png
│       ├── icon-96x96.png
│       ├── icon-128x128.png
│       ├── icon-144x144.png
│       ├── icon-152x152.png
│       ├── icon-192x192.png
│       ├── icon-384x384.png
│       └── icon-512x512.png
└── templates/
    └── index.html             # Main web interface
```

## Technical Details

### Backend
- **Framework**: Flask (Python web microframework)
- **Conversion Engine**: pypandoc (Python wrapper for Pandoc)
- **PDF Generation**: xhtml2pdf (pure Python implementation)
- **File Handling**: Python tempfile for secure temporary storage
- **Auto-open**: Python webbrowser module for launching files

### Frontend
- **Styling**: Custom CSS with CSS Grid and Flexbox
- **JavaScript**: Vanilla JS (no frameworks)
- **File Upload**: HTML5 Drag & Drop API
- **AJAX**: Fetch API for async server communication
- **PWA**: Service Worker API for offline caching and installability

### Progressive Web App
- **Service Worker**: Caches static assets, handles offline state
- **Web Manifest**: Defines app metadata, icons, and display mode
- **Install Prompts**: Native installation experience on all platforms
- **Offline UI**: Interface loads instantly from cache
- **Standalone Mode**: Runs without browser chrome when installed

### Color Palette
- Background: `#0a0a0a` (near-black)
- Red Accent: `#cc0000`
- Gold Highlight: `#d4af37`
- Secondary BG: `#1a1a1a`

## Documentation

- **README.md** (this file) - Main documentation and quick start
- **PWA-INSTALL-GUIDE.md** - Comprehensive PWA installation guide for all platforms
- **README-PWA.md** - PWA features and technical details
- **CLAUDE.md** - Original build specifications and design requirements

## Troubleshooting

### Pandoc Installation Issues
If pypandoc fails to auto-download Pandoc:
- Check your internet connection
- Try manual installation from [pandoc.org](https://pandoc.org/installing.html)
- Verify firewall settings allow downloads

### Port Already in Use
If port 5000 is already in use, modify `app.py` line 219:
```python
app.run(debug=True, host='localhost', port=5001)  # Change port number
```

### Conversion Failures
- Verify your input file is not corrupted
- Check that the input format is supported
- Ensure the file size is under 50MB
- Review the error message in the status bar
- Check browser console (F12) for detailed error messages

### File Won't Open (Convert & Open)
- Ensure you have a default application set for the output format
- Try "Convert & Download" instead and open manually
- On Linux, verify xdg-utils is installed for file opening

### PWA Installation Issues
- **Install button doesn't appear**: Clear browser cache, ensure icons are generated
- **Service Worker fails to register**: Check browser console for errors
- **Icons not showing**: Verify `static/icons/` contains all 8 PNG files
- **Offline mode not working**: Ensure service worker is activated (check DevTools)

For detailed PWA troubleshooting, see `PWA-INSTALL-GUIDE.md`.

### Network Access for Mobile Devices
To access the converter from mobile devices on your local network:

1. Find your computer's IP address:
   - Windows: `ipconfig`
   - macOS/Linux: `ifconfig` or `ip addr show`

2. Edit `app.py` line 219:
   ```python
   app.run(debug=True, host='0.0.0.0', port=5000)
   ```

3. On mobile, navigate to `http://YOUR_IP:5000`

4. On Windows, you may need to allow Python through the firewall

## Security Notes

- This application is designed for **local use only**
- Debug mode is enabled by default - **DO NOT** expose to the internet
- All files are processed locally - no data is sent to external servers
- Temporary files are automatically cleaned up after conversion
- When using `host='0.0.0.0'`, only use on trusted networks

## Browser Support

### Desktop PWA Installation
- Chrome: Windows, macOS, Linux (Full support)
- Edge: Windows, macOS, Linux (Full support)
- Brave: Windows, macOS, Linux (Full support)
- Firefox: Windows, macOS, Linux (Limited PWA support)
- Safari: macOS (Limited PWA support)

### Mobile PWA Installation
- Chrome: Android (Full support)
- Safari: iOS (Add to Home Screen support)
- Edge: Android (Full support)
- Firefox: Android (Limited support)

## Platform-Specific Notes

### Windows
- Installed PWA appears in Start Menu
- Can be pinned to taskbar
- Firewall may prompt for network access

### macOS
- Installed PWA appears in Applications/Chrome Apps
- Can be added to Dock
- May require granting terminal permissions

### Linux (Arch)
- Installed PWA appears in application menu
- Desktop file created automatically
- Works with all major desktop environments

### iOS
- Uses "Add to Home Screen" feature
- Appears on home screen with RAIS icon
- Opens in standalone mode

### Android
- Native install prompt
- Appears in app drawer
- Full PWA feature support

## Future Enhancements

Planned features (marked with TODO comments in code):
- Batch conversion (multiple files at once)
- Conversion history log
- Custom output location selector
- Format-specific conversion options (margins, fonts, etc.)
- Background sync for offline conversions
- Push notifications for conversion completion
- Share target (receive files from other apps)
- File handling (open files directly in converter)

## Support

For issues or questions:
- Check the Troubleshooting section above
- Review `PWA-INSTALL-GUIDE.md` for installation issues
- Check error messages in the browser console (F12)
- Verify Python version: `python --version` (requires 3.8+)
- Verify all dependencies installed: `pip list`

## License

Internal RAIS tool - for team use only.

---

**RAIS Document Converter**
Advanced Document Transformation System
Recursive Self-Improvement Team
