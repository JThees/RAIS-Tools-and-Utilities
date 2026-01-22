# RAIS Document Converter - Progressive Web App Documentation

Technical documentation for the PWA implementation of the RAIS Document Converter.

## Overview

The RAIS Document Converter has been enhanced with Progressive Web App (PWA) capabilities, enabling installation and offline functionality across all major platforms.

## PWA Architecture

### Core Components

1. **Service Worker** (`static/service-worker.js`)
2. **Web App Manifest** (`static/manifest.json`)
3. **Application Icons** (`static/icons/`)
4. **Installation Prompts** (integrated in `templates/index.html`)

### Service Worker Implementation

**File**: `static/service-worker.js`
**Version**: 1.0.0
**Cache Name**: `rais-converter-v1`

#### Features

- **Install Event**: Caches static assets on first visit
- **Activate Event**: Cleans up old caches on update
- **Fetch Event**: Implements cache-first strategy for static resources
- **Message Handlers**: Supports cache clearing and skip waiting
- **Sync Event**: Prepared for background sync implementation
- **Push Event**: Prepared for push notification implementation

#### Caching Strategy

**Cache-First for Static Assets**:
- `/` (main HTML)
- `/static/style.css`
- `/static/logo.png`
- `/static/manifest.json`
- `/static/icons/*.png`

**Network-Only for Dynamic Endpoints**:
- `/convert` (file conversion)
- `/health` (health check)

#### Service Worker Lifecycle

1. **Install**: Downloads and caches static assets
2. **Waiting**: Waits for old service worker to finish
3. **Activate**: Takes control and cleans old caches
4. **Fetch**: Intercepts network requests for caching

### Web App Manifest

**File**: `static/manifest.json`

#### Configuration

```json
{
  "name": "RAIS Document Converter",
  "short_name": "RAIS Convert",
  "description": "Advanced Document Transformation System",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#0a0a0a",
  "theme_color": "#cc0000",
  "orientation": "any"
}
```

#### Icon Specifications

The manifest defines 8 icon sizes for optimal display across devices:

| Size | Purpose | Platforms |
|------|---------|-----------|
| 72x72 | Small icon | Android notifications |
| 96x96 | Small icon | Android launcher (low DPI) |
| 128x128 | Medium icon | Chrome Web Store |
| 144x144 | Medium icon | Windows tiles |
| 152x152 | Medium icon | iOS (legacy) |
| 192x192 | Large icon | Android launcher, PWA install |
| 384x384 | Extra large | High DPI displays |
| 512x512 | Maximum | Splash screens, high DPI |

**Maskable Icons**: 192x192 and 512x512 marked as maskable for adaptive icons

#### Display Modes

- **standalone**: App runs in its own window without browser UI
- **fullscreen**: Not used (would hide system UI)
- **minimal-ui**: Not used (shows minimal browser controls)
- **browser**: Fallback mode if standalone not supported

### Application Icons

**Location**: `static/icons/`
**Format**: PNG with transparency (RGBA)
**Optimization**: Compressed with Pillow

#### Generation

Icons are generated from `static/logo.png` using `generate-icons.py`:

```bash
python generate-icons.py
```

**Process**:
1. Load source image (RAIS hexagon logo)
2. Convert to RGBA mode for transparency
3. Resize using LANCZOS resampling (high quality)
4. Optimize PNG compression
5. Save to `static/icons/`

#### Icon Requirements

All icons must:
- Be PNG format
- Include transparency (RGBA)
- Match exact dimensions (e.g., 192x192 for icon-192x192.png)
- Be optimized for file size
- Maintain visual clarity at all sizes

### HTML Integration

**File**: `templates/index.html`

#### PWA Meta Tags

```html
<!-- Theme and mobile web app -->
<meta name="theme-color" content="#cc0000">
<meta name="mobile-web-app-capable" content="yes">

<!-- Apple iOS specific -->
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="RAIS Convert">

<!-- Manifest link -->
<link rel="manifest" href="/static/manifest.json">

<!-- Icon links -->
<link rel="icon" sizes="192x192" href="/static/icons/icon-192x192.png">
<link rel="apple-touch-icon" href="/static/icons/icon-192x192.png">
```

#### Service Worker Registration

```javascript
if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/service-worker.js')
        .then(registration => {
            // Handle updates
            registration.addEventListener('updatefound', () => {
                const newWorker = registration.installing;
                // Notify user of updates
            });
        });
}
```

#### Install Prompt Handling

```javascript
let deferredPrompt;

window.addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault();
    deferredPrompt = e;
    // Could show custom install UI
});

window.addEventListener('appinstalled', (e) => {
    console.log('PWA installed successfully');
});
```

### Flask Integration

**File**: `app.py`

#### Service Worker Route

```python
@app.route('/service-worker.js')
def service_worker():
    """Serve the service worker file"""
    return send_file('static/service-worker.js',
                     mimetype='application/javascript')
```

**Important**: Service worker must be served from root scope with correct MIME type.

## Installation Process

### Desktop Installation Flow

1. User navigates to `http://localhost:5000`
2. Browser loads HTML and registers service worker
3. Service worker caches static assets
4. Browser detects PWA installability criteria
5. Install icon appears in address bar
6. User clicks install icon
7. Browser shows install dialog
8. User confirms installation
9. PWA launches in standalone window
10. Desktop shortcut/menu entry created

### Mobile Installation Flow

#### iOS (Safari)
1. User navigates to server IP in Safari
2. Manifest and icons detected
3. User taps Share button
4. User selects "Add to Home Screen"
5. Icon appears on home screen
6. Tap launches in standalone mode

#### Android (Chrome)
1. User navigates to server IP in Chrome
2. PWA installability criteria checked
3. Install banner appears (or manual via menu)
4. User taps "Install"
5. App added to app drawer
6. Launch icon opens standalone app

## Offline Capabilities

### Currently Cached (Offline Available)

- HTML interface (`/`)
- CSS stylesheet
- JavaScript code
- RAIS logo
- App icons
- Web manifest

### Requires Network (Not Cached)

- File conversions (`/convert`)
- Health checks (`/health`)
- Uploaded files
- Downloaded conversions

### Future Offline Enhancements

**Background Sync**:
- Queue conversion requests when offline
- Process queue when connection restored
- Notify user of completion

**IndexedDB Storage**:
- Store conversion history
- Cache frequently converted files
- Persist user preferences

## Platform Support

### Desktop

**Windows**:
- Chrome: Full support
- Edge: Full support
- Brave: Full support
- Firefox: Limited (experimental PWA support)

**macOS**:
- Chrome: Full support
- Edge: Full support
- Brave: Full support
- Safari: Limited (no install prompt)

**Linux**:
- Chrome: Full support
- Brave: Full support
- Firefox: Limited (requires flags enabled)

### Mobile

**iOS**:
- Safari: Add to Home Screen support
- Chrome: No install (uses Safari engine)
- Must use Safari's "Add to Home Screen" feature
- No true background functionality

**Android**:
- Chrome: Full PWA support
- Edge: Full PWA support
- Firefox: Limited support
- Native install prompts and background capability

## Security Considerations

### Service Worker Scope

Service workers can only control resources within their scope:
- Registered at `/service-worker.js`
- Controls all routes under `/`
- Cannot access external domains

### HTTPS Requirement

PWAs require HTTPS except for localhost:
- Development: `http://localhost:5000` (allowed)
- Production: Must use HTTPS
- Service worker won't register over HTTP (except localhost)

### Content Security Policy

Consider adding CSP headers for production:
```python
@app.after_request
def add_security_headers(response):
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    return response
```

### Network Binding

**localhost** (`host='localhost'`):
- Only accessible from local machine
- Secure for development
- Cannot install on mobile devices

**0.0.0.0** (`host='0.0.0.0'`):
- Accessible from network
- Required for mobile installation
- Use only on trusted networks

## Performance Optimizations

### Service Worker Caching

- **Cache-first**: Static assets load instantly from cache
- **Network fallback**: Ensures fresh content when available
- **Precaching**: Critical resources cached on install
- **Cache versioning**: Old caches cleaned on update

### Icon Optimization

- PNG compression with Pillow `optimize=True`
- LANCZOS resampling for quality
- Appropriate sizes prevent upscaling/downscaling
- Transparency preserved for modern platforms

### Manifest Optimization

- Minimal JSON structure
- No unnecessary metadata
- Optimized icon references
- Fast parsing

## Future Enhancements

### Planned Features

**Background Sync**:
```javascript
// In service worker
self.addEventListener('sync', (event) => {
    if (event.tag === 'sync-conversions') {
        event.waitUntil(processQueuedConversions());
    }
});
```

**Push Notifications**:
```javascript
// In service worker
self.addEventListener('push', (event) => {
    const options = {
        body: 'Your document conversion is complete',
        icon: '/static/icons/icon-192x192.png'
    };
    event.waitUntil(
        self.registration.showNotification('RAIS Converter', options)
    );
});
```

**File Handling**:
```json
// In manifest.json
"file_handlers": [{
    "action": "/",
    "accept": {
        "text/markdown": [".md"],
        "application/pdf": [".pdf"]
    }
}]
```

**Share Target**:
```json
// In manifest.json
"share_target": {
    "action": "/convert",
    "method": "POST",
    "enctype": "multipart/form-data",
    "params": {
        "files": [{
            "name": "file",
            "accept": ["text/*", "application/*"]
        }]
    }
}
```

## Debugging

### Chrome DevTools

**Application Tab**:
- Service Workers: View registration status
- Manifest: Verify manifest.json parsing
- Cache Storage: Inspect cached resources
- Clear Storage: Reset PWA state

**Console**:
- Service worker lifecycle logs
- Cache operation logs
- Install event tracking

**Network Tab**:
- View cache hits vs network requests
- Test offline mode
- Monitor service worker activity

### Testing Checklist

- [ ] Service worker registers successfully
- [ ] All icons load without errors
- [ ] Manifest parses correctly
- [ ] Install prompt appears
- [ ] App installs to desktop/home screen
- [ ] Standalone mode works
- [ ] Offline UI loads from cache
- [ ] Cache updates on reload
- [ ] Uninstall works properly

## Deployment

### Development

```bash
python app.py
# Server runs on http://localhost:5000
# Service worker registers
# Install available immediately
```

### Production

1. **Use production WSGI server**:
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:443 app:app
   ```

2. **Enable HTTPS**:
   - Obtain SSL certificate
   - Configure with `--certfile` and `--keyfile`
   - Update manifest `start_url` to domain

3. **Disable debug mode**:
   ```python
   app.run(debug=False, host='0.0.0.0', port=443)
   ```

4. **Update service worker version** on each deployment

## Technical Specifications

### Requirements

- Python 3.8+
- Flask 2.0+
- Modern browser with service worker support
- HTTPS for production (optional for localhost)

### Dependencies

```
Flask>=2.0
pypandoc>=1.5
xhtml2pdf>=0.2
Pillow>=9.0
```

### File Sizes

- Service worker: ~5KB
- Manifest: ~1KB
- Icons (total): ~600KB (all 8 sizes)
- Total PWA overhead: ~606KB

### Browser APIs Used

- Service Worker API
- Cache API
- Fetch API
- Notifications API (prepared)
- Background Sync API (prepared)
- Web App Manifest

## Standards Compliance

### W3C Standards

- Web App Manifest specification
- Service Worker specification
- Cache API specification
- Fetch API specification

### Best Practices

- Manifest includes all required fields
- Icons cover all common sizes
- Service worker handles offline gracefully
- Install criteria met for all platforms
- Accessibility maintained in standalone mode

## Troubleshooting

See `PWA-INSTALL-GUIDE.md` for comprehensive troubleshooting guide.

## References

- **W3C Web App Manifest**: https://www.w3.org/TR/appmanifest/
- **Service Worker Spec**: https://www.w3.org/TR/service-workers/
- **MDN PWA Guide**: https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps
- **Google PWA Checklist**: https://web.dev/pwa-checklist/

---

**RAIS Document Converter**
Progressive Web App Technical Documentation
Version 1.0
