# RAIS Document Converter - Documentation Index

Complete documentation for the RAIS Document Converter Progressive Web Application.

## Quick Start

**New User?** Start here:
1. Read [Installation](#installation-guides) for your platform
2. Run the installation script
3. Follow [PWA Installation Guide](#pwa-installation-guide) to install the app

**Developer?** Check:
1. [Technical Documentation](#technical-documentation) for architecture details
2. [Project Structure](#project-structure) for file organization
3. [Build Specifications](#build-specifications) for design requirements

## Available Documentation

### Main Documentation

**README.md** - Primary documentation
- Overview and features
- Quick start guide (automated installation scripts)
- Manual installation instructions
- Usage instructions
- Project structure
- Technical details (backend, frontend, PWA)
- Troubleshooting guide
- Browser support matrix
- Platform-specific notes
- Future enhancements

### PWA Installation Guide

**PWA-INSTALL-GUIDE.md** - Comprehensive installation guide
- Desktop installation (Windows, macOS, Linux)
- Mobile installation (iOS, Android)
- Network configuration for mobile access
- Verification procedures
- Detailed troubleshooting
- Advanced configuration (HTTPS, reverse proxy, etc.)
- Platform-specific instructions
- Firewall configuration

### PWA Technical Documentation

**README-PWA.md** - Technical PWA documentation
- PWA architecture overview
- Service worker implementation
- Web manifest configuration
- Icon specifications
- Installation process flows
- Offline capabilities
- Platform support details
- Security considerations
- Performance optimizations
- Future enhancements (background sync, push notifications)
- Debugging guide
- Deployment instructions
- Standards compliance

### Build Specifications

**CLAUDE.md** - Original project requirements
- Project overview
- Visual design specifications
- Technical stack
- Supported conversions
- User flow
- File structure
- Error handling requirements
- Branding guidelines

## Installation Guides

### Windows

1. **Automated Installation**
   - Run `WinInstall.bat` - Installs all dependencies
   - Run `WinRun.bat` - Launches the server

2. **Manual Installation**
   - See README.md → Manual Installation section
   - Requires Python 3.8+, pip

### macOS

1. **Automated Installation**
   ```bash
   chmod +x MacInstall.sh MacRun.sh
   ./MacInstall.sh    # Install dependencies
   ./MacRun.sh        # Launch server
   ```

2. **Manual Installation**
   - See README.md → Manual Installation section
   - Requires Python 3.8+, pip

### Linux (Arch)

1. **Automated Installation**
   ```bash
   chmod +x ArchInstall.sh ArchRun.sh
   ./ArchInstall.sh   # Install dependencies
   ./ArchRun.sh       # Launch server
   ```

2. **Manual Installation**
   - See README.md → Manual Installation section
   - Requires Python 3.8+, pip

## File Organization

### Documentation Files

```
raix-file-converter/
├── README.md                 # Main documentation
├── PWA-INSTALL-GUIDE.md      # PWA installation guide
├── README-PWA.md             # PWA technical documentation
├── CLAUDE.md                 # Build specifications
├── DOCUMENTATION.md          # This file (documentation index)
└── LICENSE                   # License information
```

### Installation Scripts

```
raix-file-converter/
├── WinInstall.bat           # Windows installation
├── WinRun.bat               # Windows launcher
├── MacInstall.sh            # macOS installation
├── MacRun.sh                # macOS launcher
├── ArchInstall.sh           # Arch Linux installation
├── ArchRun.sh               # Arch Linux launcher
└── generate-icons.py        # PWA icon generator
```

### Application Files

```
raix-file-converter/
├── app.py                   # Flask backend
├── requirements.txt         # Python dependencies
├── static/
│   ├── logo.png            # RAIS hexagon logo
│   ├── style.css           # Cyberpunk theme
│   ├── manifest.json       # PWA manifest
│   ├── service-worker.js   # Service worker
│   └── icons/              # PWA icons (8 sizes)
└── templates/
    └── index.html          # Main interface
```

## Common Tasks

### First-Time Setup

1. Choose your platform (Windows, macOS, Linux)
2. Run the installation script for your platform
3. Installation script will:
   - Verify Python installation
   - Install all dependencies
   - Generate PWA icons
   - Prepare application

### Running the Application

**Automated:**
- Windows: `WinRun.bat`
- macOS: `./MacRun.sh`
- Linux: `./ArchRun.sh`

**Manual:**
```bash
python app.py
```

Access at: `http://localhost:5000`

### Installing as PWA

**Desktop (Windows/Mac/Linux):**
1. Start server
2. Open Chrome, Edge, or Brave
3. Navigate to `http://localhost:5000`
4. Click install icon in address bar
5. Click "Install"

**Mobile (iOS/Android):**
- See PWA-INSTALL-GUIDE.md for detailed instructions
- Requires network configuration

### Regenerating Icons

If you update the RAIS logo:

```bash
python generate-icons.py
```

This creates all 8 required PWA icon sizes.

### Troubleshooting

**Issue with installation?**
- See README.md → Troubleshooting section

**Issue with PWA installation?**
- See PWA-INSTALL-GUIDE.md → Troubleshooting section

**Technical questions?**
- See README-PWA.md for detailed technical information

## Documentation Standards

All documentation follows these standards:
- Professional tone
- Clear, structured formatting
- Platform-specific instructions where needed
- Complete troubleshooting sections
- Version information included
- No emojis or informal language

## Support Resources

### For End Users
1. README.md - Start here
2. PWA-INSTALL-GUIDE.md - For installation help
3. Troubleshooting sections in both documents

### For Developers
1. README-PWA.md - Technical details
2. CLAUDE.md - Original specifications
3. Source code comments in:
   - app.py (Flask backend)
   - service-worker.js (PWA caching)
   - index.html (Frontend functionality)

### For System Administrators
1. PWA-INSTALL-GUIDE.md → Advanced Configuration
   - HTTPS setup
   - Reverse proxy (Nginx)
   - Firewall configuration
   - Production deployment

## Version Information

**Current Version**: 1.0
**Documentation Last Updated**: December 2024
**PWA Version**: 1.0.0
**Service Worker Cache**: rais-converter-v1

## Quick Reference

### Supported Formats

**Input**: MD, TXT, DOCX, HTML, ODT, RTF
**Output**: MD, TXT, PDF, DOCX, HTML

**Note**: PDF is output-only (Pandoc limitation)

### System Requirements

- Python 3.8 or higher
- pip (Python package installer)
- Modern browser (Chrome, Edge, Brave recommended)
- 50MB max file size

### Dependencies

- Flask (web framework)
- pypandoc (document conversion)
- xhtml2pdf (PDF generation)
- Pillow (icon generation)

### Default Configuration

- **Server**: http://localhost:5000
- **Port**: 5000 (configurable)
- **Host**: localhost (change to 0.0.0.0 for network access)
- **Debug Mode**: Enabled (disable for production)
- **Max File Size**: 50MB

## Getting Help

1. **Check documentation** (start with README.md)
2. **Review troubleshooting sections**
3. **Check browser console** (F12) for errors
4. **Verify installation** completed successfully
5. **Test with different browser** if issues persist

## Contributing

This is an internal RAIS tool. For modifications:
1. Review CLAUDE.md for design requirements
2. Check README-PWA.md for PWA architecture
3. Test on all platforms before deployment
4. Update documentation to reflect changes
5. Increment service worker version if modifying PWA

## License

Internal RAIS tool - for team use only.

---

**RAIS Document Converter**
Documentation Index
Version 1.0
