# RAIS Document Converter - PWA Installation Guide

Complete installation guide for deploying the RAIS Document Converter as a Progressive Web App across all supported platforms.

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Desktop Installation](#desktop-installation)
4. [Mobile Installation](#mobile-installation)
5. [Network Configuration](#network-configuration)
6. [Verification](#verification)
7. [Troubleshooting](#troubleshooting)
8. [Advanced Configuration](#advanced-configuration)

## Overview

The RAIS Document Converter is configured as a Progressive Web App (PWA), enabling installation on:

- **Windows** (Chrome, Edge, Brave)
- **macOS** (Chrome, Edge, Safari)
- **Linux** (Chrome, Firefox, Brave)
- **iOS** (Safari)
- **Android** (Chrome, Edge)

### PWA Components

- **Service Worker** (`static/service-worker.js`) - Handles caching and offline functionality
- **Web Manifest** (`static/manifest.json`) - Defines app metadata and branding
- **App Icons** (`static/icons/`) - 8 optimized icon sizes (72px to 512px)
- **Install Prompts** - Native installation experience on all platforms

## Prerequisites

Before installing the PWA, ensure:

1. Server is running (use platform-specific run script)
2. PWA icons have been generated (`python generate-icons.py`)
3. Browser supports PWA installation (see compatibility table below)

### Browser Compatibility

| Browser | Windows | macOS | Linux | iOS | Android |
|---------|---------|-------|-------|-----|---------|
| Chrome  | Yes     | Yes   | Yes   | No  | Yes     |
| Edge    | Yes     | Yes   | Yes   | No  | Yes     |
| Safari  | No      | Limited | No  | Yes | No      |
| Firefox | Limited | Limited | Limited | No | Limited |
| Brave   | Yes     | Yes   | Yes   | No  | Yes     |

**Recommended**: Chrome, Edge, or Brave for full PWA support.

## Desktop Installation

### Windows (Chrome, Edge, Brave)

1. **Start the server**
   ```cmd
   WinRun.bat
   ```

2. **Open supported browser**
   - Launch Chrome, Edge, or Brave

3. **Navigate to application**
   ```
   http://localhost:5000
   ```

4. **Install the PWA**
   - Method 1: Click the install icon in the address bar (plus symbol or computer icon, usually on the right side)
   - Method 2: Click browser menu (three dots) → "Apps" → "Install RAIS Document Converter"

5. **Confirm installation**
   - Click "Install" in the popup dialog
   - The app will open in a new standalone window

6. **Access installed app**
   - Windows Start Menu → Search "RAIS Document Converter"
   - Pin to taskbar for quick access

### macOS (Chrome, Edge)

1. **Start the server**
   ```bash
   ./MacRun.sh
   ```

2. **Open supported browser**
   - Launch Chrome or Edge (recommended)
   - Safari has limited PWA support

3. **Navigate to application**
   ```
   http://localhost:5000
   ```

4. **Install the PWA**
   - Click install icon in address bar
   - Or: Browser menu → "Install RAIS Document Converter"

5. **Access installed app**
   - Applications → Chrome Apps → RAIS Document Converter
   - Add to Dock for quick access

### Linux (Chrome, Brave)

1. **Start the server**
   ```bash
   ./ArchRun.sh
   ```

2. **Open supported browser**
   - Launch Chrome or Brave

3. **Navigate to application**
   ```
   http://localhost:5000
   ```

4. **Install the PWA**
   - Click install icon in address bar
   - Or: Browser menu → "Install RAIS Document Converter"

5. **Access installed app**
   - Application menu (location varies by desktop environment)
   - Desktop file created automatically

## Mobile Installation

Mobile installation requires network access to reach the server from your phone or tablet.

### Network Setup (Required for Mobile)

1. **Find your computer's IP address**

   **Windows:**
   ```cmd
   ipconfig
   ```
   Look for "IPv4 Address" (e.g., `192.168.1.100`)

   **macOS:**
   ```bash
   ifconfig | grep "inet "
   ```

   **Linux:**
   ```bash
   ip addr show
   ```
   or
   ```bash
   hostname -I
   ```

2. **Enable network access**

   Edit `app.py` line 219:

   **Change from:**
   ```python
   app.run(debug=True, host='localhost', port=5000)
   ```

   **To:**
   ```python
   app.run(debug=True, host='0.0.0.0', port=5000)
   ```

3. **Configure firewall (Windows only)**
   - Windows Defender may block incoming connections
   - Allow Python through firewall when prompted
   - Or manually: Windows Defender Firewall → Allow an app → Python

4. **Verify connection**
   - Ensure computer and mobile device are on the same WiFi network
   - Test by opening `http://YOUR_IP:5000` in mobile browser

### iOS Installation (iPhone, iPad)

1. **Open Safari browser**
   - PWA installation on iOS requires Safari
   - Other browsers cannot install PWAs on iOS

2. **Navigate to server**
   ```
   http://YOUR_IP:5000
   ```
   Example: `http://192.168.1.100:5000`

3. **Add to Home Screen**
   - Tap the Share button (square with arrow pointing up)
   - Scroll down and tap "Add to Home Screen"
   - Edit name if desired (default: "RAIS Convert")
   - Tap "Add" in the top-right corner

4. **Access installed app**
   - App icon appears on home screen
   - Tap icon to launch in standalone mode
   - Runs without Safari browser chrome

### Android Installation (Phone, Tablet)

1. **Open Chrome browser**
   - Chrome provides the best PWA experience on Android
   - Edge also supports PWA installation

2. **Navigate to server**
   ```
   http://YOUR_IP:5000
   ```
   Example: `http://192.168.1.100:5000`

3. **Install the app**
   - Method 1: Tap install banner when it appears at bottom of screen
   - Method 2: Tap menu (three dots) → "Install app" or "Add to Home Screen"

4. **Confirm installation**
   - Tap "Install" in the dialog

5. **Access installed app**
   - App appears in app drawer
   - Tap to launch in standalone mode
   - Behaves like a native Android app

## Network Configuration

### Local Network Access

To make the server accessible to other devices on your network:

1. Edit `app.py` to bind to all network interfaces:
   ```python
   app.run(debug=True, host='0.0.0.0', port=5000)
   ```

2. Find your computer's local IP address (see Mobile Installation section)

3. Access from other devices using: `http://YOUR_IP:5000`

### Security Considerations

When binding to `0.0.0.0`:
- Server is accessible to ANY device on your network
- Safe for trusted networks (home, office)
- **NOT SAFE** for public/untrusted networks
- Debug mode should remain disabled in production

For public deployment:
- Use production WSGI server (Gunicorn, uWSGI)
- Enable HTTPS with SSL certificate
- Disable debug mode
- Implement authentication if needed

### Firewall Configuration

**Windows Firewall:**
- Windows Defender → Firewall & network protection
- Allow an app through firewall → Python
- Enable both Private and Public networks (or Private only for security)

**macOS Firewall:**
- System Preferences → Security & Privacy → Firewall
- Firewall Options → Add Python
- Allow incoming connections

**Linux Firewall (ufw):**
```bash
sudo ufw allow 5000/tcp
sudo ufw reload
```

## Verification

### Verify Service Worker Registration

1. Open the app in browser
2. Press F12 to open Developer Tools
3. Navigate to **Application** tab (Chrome/Edge) or **Storage** tab (Firefox)
4. Click **Service Workers** in sidebar
5. Verify status shows: "Activated and running"
6. Service worker URL should be: `/service-worker.js`

### Verify Web Manifest

1. In Developer Tools → **Application** tab
2. Click **Manifest** in sidebar
3. Verify the following:
   - **Name**: "RAIS Document Converter"
   - **Short name**: "RAIS Convert"
   - **Start URL**: "/"
   - **Display**: "standalone"
   - **Theme color**: #cc0000 (red)
   - **Background color**: #0a0a0a (black)

4. Check icons section:
   - Should show 8 icon entries
   - Sizes: 72x72, 96x96, 128x128, 144x144, 152x152, 192x192, 384x384, 512x512
   - All icons should have preview images

### Test Offline Functionality

1. Open the app while connected to server
2. Open Developer Tools (F12)
3. Navigate to **Network** tab
4. Check "Offline" checkbox (or select "Offline" from throttling dropdown)
5. Refresh the page (F5 or Ctrl+R)
6. App interface should still load from cache
7. Note: Actual conversions require server connection

### Test Installed App

1. Close browser
2. Launch app from:
   - Windows: Start Menu
   - macOS: Applications/Chrome Apps or Dock
   - Linux: Application menu
   - iOS: Home screen
   - Android: App drawer

3. Verify app opens in standalone window (no browser address bar/tabs)
4. Test file conversion functionality
5. Check that RAIS branding appears correctly

## Troubleshooting

### Install Button Not Appearing

**Cause**: PWA requirements not met

**Solutions**:
1. Clear browser cache (Ctrl+Shift+Delete)
2. Verify all icons exist in `static/icons/` folder
3. Run `python generate-icons.py` to regenerate icons
4. Check browser console (F12) for errors
5. Ensure manifest.json is valid (check Application tab)
6. Try different browser (Chrome/Edge recommended)
7. Verify service worker registered successfully

### Service Worker Not Registering

**Cause**: JavaScript errors or file not served correctly

**Solutions**:
1. Check browser console for error messages
2. Verify `static/service-worker.js` file exists
3. Check Flask route serves service worker: `http://localhost:5000/service-worker.js`
4. Ensure no browser extensions blocking service workers
5. Try in private/incognito mode
6. Clear site data: DevTools → Application → Storage → Clear site data

### Icons Not Displaying

**Cause**: Icon files missing or paths incorrect

**Solutions**:
1. Verify `static/icons/` directory exists
2. Check all 8 icon files are present:
   ```bash
   ls -la static/icons/
   ```
3. Regenerate icons:
   ```bash
   python generate-icons.py
   ```
4. Verify file names are exact (case-sensitive):
   - `icon-72x72.png`
   - `icon-96x96.png`
   - `icon-128x128.png`
   - `icon-144x144.png`
   - `icon-152x152.png`
   - `icon-192x192.png`
   - `icon-384x384.png`
   - `icon-512x512.png`
5. Clear browser cache and hard reload (Ctrl+Shift+R)

### Cannot Access from Mobile Device

**Cause**: Network configuration or firewall blocking

**Solutions**:
1. Verify devices on same WiFi network
2. Confirm server bound to `0.0.0.0` not `localhost`
3. Check firewall allows port 5000
4. Verify correct IP address (not 127.0.0.1 or localhost)
5. Try accessing from mobile browser first: `http://YOUR_IP:5000`
6. Test with computer firewall temporarily disabled
7. Check router settings (some routers block inter-device communication)

### Offline Mode Not Working

**Cause**: Service worker not caching correctly

**Solutions**:
1. Visit site while online first (service worker must install)
2. Check service worker status: DevTools → Application → Service Workers
3. Verify status shows "Activated and running"
4. Check Cache Storage: DevTools → Application → Cache Storage
5. Should see cache named `rais-converter-v1`
6. Clear caches and reload to reinstall service worker
7. Check browser console for service worker errors

### iOS: Cannot Install PWA

**Cause**: iOS requires specific browser and steps

**Solutions**:
1. Must use Safari browser (Chrome/Firefox won't work on iOS)
2. Navigate to correct URL with IP address
3. Use Share button → "Add to Home Screen" (not browser menu)
4. Ensure manifest.json contains apple-specific meta tags
5. Check that icon-192x192.png exists (used for iOS icon)
6. Try restarting Safari
7. Update iOS to latest version

### Android: Install Banner Not Showing

**Cause**: PWA criteria not met or already installed

**Solutions**:
1. Ensure using Chrome browser
2. PWA install criteria must be met:
   - Valid manifest.json
   - Service worker registered
   - Served over HTTPS or localhost
   - Icons present
3. If previously installed, uninstall first
4. Clear Chrome data for site
5. Use manual install: Menu → "Install app"
6. Check Chrome flags: `chrome://flags` → Search "PWA"

### Windows: Firewall Blocking Connections

**Cause**: Windows Defender blocking Python

**Solutions**:
1. Allow Python through firewall:
   - Windows Defender Firewall
   - Allow an app through firewall
   - Change settings → Allow another app
   - Browse to Python executable
   - Enable both Private and Public networks
2. Or create firewall rule for port 5000:
   ```cmd
   netsh advfirewall firewall add rule name="RAIS Converter" dir=in action=allow protocol=TCP localport=5000
   ```
3. Temporarily disable firewall to test (re-enable after)

## Advanced Configuration

### Custom Port Configuration

If port 5000 is in use, change the port:

Edit `app.py` line 219:
```python
app.run(debug=True, host='0.0.0.0', port=8080)  # Change to desired port
```

Also update mobile access URL: `http://YOUR_IP:8080`

### HTTPS Configuration (Production)

For production deployment with HTTPS:

1. **Obtain SSL certificate** (Let's Encrypt, commercial CA, self-signed)

2. **Install production WSGI server**:
   ```bash
   pip install gunicorn
   ```

3. **Run with SSL**:
   ```bash
   gunicorn --bind 0.0.0.0:443 --certfile cert.pem --keyfile key.pem app:app
   ```

4. **Update manifest.json** `start_url` to production domain

### Reverse Proxy Setup (Nginx)

For production deployment behind Nginx:

```nginx
server {
    listen 80;
    server_name converter.rais.example.com;

    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /service-worker.js {
        proxy_pass http://localhost:5000/service-worker.js;
        add_header Service-Worker-Allowed /;
        add_header Cache-Control "no-cache";
    }
}
```

### Update Service Worker Version

When updating the app, increment service worker version:

Edit `static/service-worker.js` line 4:
```javascript
const CACHE_NAME = 'rais-converter-v2';  // Increment version number
```

This forces clients to download updated cache.

### Enable Background Sync (Future)

The service worker includes hooks for background sync. To implement:

1. Register sync event in main JavaScript
2. Implement sync handler in service worker
3. Queue conversions when offline
4. Process queue when connection restored

### Enable Push Notifications (Future)

The service worker includes push notification handlers. To implement:

1. Request notification permission from user
2. Register push subscription
3. Send push messages from server
4. Handle in service worker push event

## Platform-Specific Notes

### Windows
- Installed PWA appears in Start Menu under "RAIS Document Converter"
- Can pin to taskbar for quick access
- Uninstall: Settings → Apps → RAIS Document Converter → Uninstall
- App data stored in: `%LOCALAPPDATA%\Google\Chrome\User Data\Default\Web Applications`

### macOS
- Installed PWA in Applications/Chrome Apps/ folder
- Add to Dock by dragging from Applications
- Uninstall: Right-click app icon → Remove
- App data in: `~/Library/Application Support/Google/Chrome/Default/Web Applications`

### Linux
- Desktop file created in `~/.local/share/applications/`
- Appears in application menu automatically
- Location varies by desktop environment (GNOME, KDE, XFCE)
- Uninstall through browser app management

### iOS
- Icon appears on home screen
- Tap to launch in standalone mode
- Remove: Long-press icon → Remove App
- No true background functionality (iOS limitation)
- Cannot access local file system
- Must use server-based conversions

### Android
- Full PWA support with background functionality
- Appears in app drawer like native app
- Can receive push notifications
- Uninstall: Settings → Apps → RAIS Document Converter → Uninstall
- Background sync supported (when implemented)

## Support

For installation issues:

1. Check this troubleshooting section
2. Verify prerequisites are met
3. Check browser console for errors (F12)
4. Ensure all files generated correctly
5. Try alternative browser
6. Refer to main README.md for general troubleshooting

## Additional Resources

- **Main Documentation**: README.md
- **PWA Features**: README-PWA.md
- **Build Specifications**: CLAUDE.md
- **Icon Generator**: `python generate-icons.py --help`

---

**RAIS Document Converter**
Progressive Web App Installation Guide
Version 1.0
