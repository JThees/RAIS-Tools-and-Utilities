# RAIS Document Converter - Build Instructions

## Project Overview
Build a local web-based document converter using Flask + pypandoc. Modern, dark-themed interface featuring RAIS branding for internal team use.

## Visual Design
- **Color Scheme**: Black background (#000000 or #0a0a0a), red accents (#cc0000), gold highlights (#d4af37)
- **Logo**: Use RAIS hexagon logo prominently at top (provided separately)
- **Style**: Clean, modern, cyberpunk aesthetic - sleek tech interface
- **Font**: Sans-serif, high contrast for readability

## Technical Stack

### Backend (Python/Flask)
```
app.py structure:
- Flask web server on localhost:5000
- Upload endpoint accepting multiple file types
- pypandoc conversion wrapper (auto-installs Pandoc binaries)
- File handling with temp directory cleanup
- Auto-open converted files with webbrowser module
- Error handling with user-friendly messages
```

### Dependencies (requirements.txt)
```
Flask
pypandoc
```
Note: pypandoc automatically downloads Pandoc binaries on first run - no manual installation needed.

### Supported Conversions
- **Input formats**: .md, .txt, .docx, .html, .odt, .rtf
- **Output formats**: .md, .txt, .pdf, .docx, .html
- **Note**: PDF can only be OUTPUT, not input (Pandoc limitation)

### Frontend (HTML/CSS/vanilla JS)
```
Layout structure:
- Header: RAIS logo centered, "Document Converter" subtitle
- Main: Large drag-drop zone (prominent, responsive)
- File info: Display selected filename and size
- Controls: Radio buttons for output format selection
- Actions: Two buttons side-by-side
  • "Convert & Download" - saves to Downloads
  • "Convert & Open" - converts and launches in default app
- Status bar: Live feedback at bottom ("Ready", "Converting...", "Complete!", errors)
```

## Styling Details
- **Drop zone**: Dashed red border, gold on hover, smooth transitions
- **Buttons**: Dark background, red borders, gold hover effects
- **Radio buttons**: Custom styled to match theme
- **Active states**: Clear visual feedback on all interactive elements
- **Responsive**: Works on different screen sizes

## User Flow
1. User drags file into drop zone OR clicks to browse
2. File name and size display below drop zone
3. User selects output format via radio buttons
4. User clicks action button:
   - "Convert & Download" → saves to Downloads folder
   - "Convert & Open" → converts, saves to temp, opens with default app
5. Status updates in real-time during conversion
6. Success/error messages display clearly

## File Structure
```
rais-converter/
├── app.py                 # Flask backend
├── requirements.txt       # Dependencies
├── static/
│   ├── logo.png          # RAIS hexagon logo
│   └── style.css         # Stylesheet
├── templates/
│   └── index.html        # Main interface
└── README.md             # Setup instructions
```

## Error Handling
Handle gracefully with clear user messages:
- pypandoc initialization failures
- Unsupported file types
- Conversion failures
- File size limits (warn if >50MB)
- File permission issues

## Future Enhancement Markers
Add TODO comments for:
- Batch conversion (multiple files at once)
- Conversion history log
- Custom output location selector
- Format-specific conversion options

## Branding
This is an internal RAIS tool. Professional but edgy aesthetic - we're the team that just announced recursive self-improvement. Interface should reflect confidence and technical competence.
