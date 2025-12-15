<div align="center">

# Resonant AI Systems TOOLS & UTILITIES

## Browser Clocks

### Built by Resonant AI Core
**Research & Development Division of Resonant AI Systems**

![License](https://img.shields.io/badge/license-Apache%202.0-blue)
![Status](https://img.shields.io/badge/status-production-brightgreen)
![Scope](https://img.shields.io/badge/scope-continuity%20tool-purple)
![Division](https://img.shields.io/badge/division-Resonant%20AI%20Core-black)

**Temporal awareness for AI conversations that persist.**

Browser extensions that automatically inject timestamps into Claude.ai and ChatGPT conversations at the API level. Built for conversation archiving, continuity systems, and temporal context preservation.
Not display overlays. Not manual timestamps. **API-level injection that survives exports and UI changes.**

</div>

---

## WHAT THIS IS

Browser Clocks is a collection of platform-specific extensions that embed precise timestamps into AI conversations.

**Included extensions:**
- **ClaudeClock** - Timestamp injection for Claude.ai conversations
- **GPTClock** - Timestamp injection for ChatGPT.com conversations

**Core functionality:**
- Automatic timestamp prepending to user messages and AI responses
- ISO 8601 format for machine parsing + human-readable time display
- Configurable timezone selection (local or 18 major timezones worldwide)
- API-level injection (intercepts fetch calls, not DOM manipulation)
- Persistent settings across browser sessions

**Format example:**
```
[2025-11-28T23:15:07.057Z] (3:15 PM PST)
What's the weather like today?
```

Timestamps are embedded in actual conversation data, not display-layer modifications. Survives UI redesigns and conversation exports.

---

## WHY IT EXISTS

AI conversation platforms lack native timestamp embedding. Exported conversations contain no temporal context. Memory systems, archival tools, and continuity frameworks require accurate timing data.

**Problem solved:**
Manual timestamp tracking is unreliable. DOM-based injection breaks when platforms update their UI. API-level interception embeds timestamps directly into conversation data, surviving exports and platform changes.

**Use cases:**
- Conversation archiving with accurate temporal metadata
- AI memory systems requiring temporal context
- Research analyzing interaction timing patterns
- Debugging AI response latency and behavior over time

Built for users who need reliable temporal context in AI conversations without depending on platform features.

---

## FEATURES

### Timestamp Generation
- **Dual injection** - Timestamps both user messages and AI responses
- **ISO 8601 + human time** - `[2025-11-28T23:15:07.057Z] (3:15 PM PST)` format
- **Configurable timezones** - Local time or 18 major timezones (US, Europe, Asia, Oceania, UTC)
- **Millisecond precision** - Accurate timing data for analysis

### API-Level Integration
- **Fetch interception** - Modifies requests/responses at API layer
- **DOM-independent** - Works regardless of UI changes
- **Export-compatible** - Timestamps included in conversation exports
- **Streaming support** - Handles Server-Sent Event (SSE) responses

### User Interface
- **Settings popup** - Clean configuration interface
- **Live preview** - Real-time timestamp display as you configure
- **Persistent storage** - Settings saved automatically across sessions
- **Non-intrusive** - Runs silently in background

### Platform Coverage
- **ClaudeClock** - Works on claude.ai
- **GPTClock** - Works on chatgpt.com and chat.openai.com

---

## REQUIREMENTS

**Browser:**
- Chrome, Edge, Brave, or Chromium-based browser
- Developer mode enabled (for unpacked extension loading)

**Platform Accounts:**
- Active account on Claude.ai (for ClaudeClock)
- Active account on ChatGPT.com (for GPTClock)

**No additional dependencies required.**

---

## INSTALLATION

### ClaudeClock (Claude.ai)

1. **Clone repository**
   ```bash
   git clone https://github.com/resonantaisystems/RAIS-Tools-and-Utilities.git
   cd RAIS-Tools-and-Utilities/utilities/browserclocks/ClaudeClock
   ```

2. **Load extension**
   - Open `chrome://extensions/` (or `edge://extensions/`, `brave://extensions/`)
   - Enable "Developer mode" (toggle in top-right)
   - Click "Load unpacked"
   - Select the `ClaudeClock` folder

3. **Configure timezone**
   - Click ClaudeClock icon in toolbar
   - Select "Use Local Time" or choose specific timezone
   - Settings save automatically

4. **Start using**
   - Navigate to [claude.ai](https://claude.ai)
   - Send a message
   - Timestamps appear automatically

### GPTClock (ChatGPT)

1. **Clone repository** (if not already done)
   ```bash
   git clone https://github.com/resonantaisystems/RAIS-Tools-and-Utilities.git
   cd RAIS-Tools-and-Utilities/utilities/browserclocks/GPTClock
   ```

2. **Load extension**
   - Open `chrome://extensions/` (or browser-specific URL)
   - Enable "Developer mode"
   - Click "Load unpacked"
   - Select the `GPTClock` folder

3. **Configure timezone**
   - Click GPTClock icon in toolbar
   - Select timezone preference
   - Settings apply immediately

4. **Start using**
   - Navigate to [chatgpt.com](https://chatgpt.com)
   - Send a message
   - Timestamps appear automatically

---

## USAGE

### Normal Operation

Extensions run automatically once installed. No manual activation required.

**Conversation flow:**
1. Type message in Claude or ChatGPT
2. Press Enter or click Send
3. Extension intercepts request
4. Timestamp prepended to message
5. AI responds
6. Extension intercepts response
7. Timestamp prepended to AI message

**Result:**
```
[2025-11-28T15:30:45.123Z] (3:30 PM EST)
What's the weather like?

[2025-11-28T15:30:47.456Z] (3:30 PM EST)
I don't have access to real-time weather data...
```

### Timezone Configuration

**Local time mode (recommended):**
- Automatically uses browser's timezone
- Updates for Daylight Saving Time changes
- No manual configuration needed

**Specific timezone mode:**
- Choose from 18 major timezones
- US: Eastern, Central, Mountain, Pacific, Alaska, Hawaii
- Europe: London, Paris, Berlin, Moscow
- Asia: Dubai, India, China, Tokyo, Seoul
- Oceania: Sydney, Auckland
- UTC

### Settings Management

1. Click extension icon in toolbar
2. Select timezone mode
3. View live preview of timestamp format
4. Changes save automatically
5. Refresh Claude/ChatGPT page if needed

---

## STATUS & ROADMAP

**Current Status:** Production

Browser Clocks extensions are stable and actively used. ClaudeClock tested extensively on Arch Linux (Chrome/Chromium) and Windows (Chrome/Edge). GPTClock tested on multiple platforms.

**Known Limitations:**
- Chromium-based browsers only (Firefox requires compatibility patches)
- Requires developer mode for unpacked extension loading
- Platform UI changes may require extension updates (rare)
- No mobile browser support

**Tested Platforms:**

ClaudeClock:
- Linux (Arch): Chrome, Chromium ✓
- Windows: Chrome, Edge ✓
- macOS: Chrome (expected working, not extensively tested)

GPTClock:
- Chrome/Edge/Brave: All platforms ✓

**Roadmap:**
- **Firefox support** - Port to WebExtensions API for Firefox compatibility
- **Mobile browser support** - Investigate mobile extension feasibility
- **Additional platforms** - Perplexity, Gemini, other AI chat interfaces
- **Advanced formatting** - User-configurable timestamp format templates
- **Export enhancements** - Direct conversation export with preserved timestamps

**Maintenance:** Active. Extensions updated when Claude or ChatGPT API changes break functionality.

---

## ARCHITECTURE

### Two-Script Injection Pattern

**Content Script:**
- Loads user preferences from Chrome storage
- Injects interceptor script into page context
- Sends settings to page via postMessage

**Injected Script:**
- Runs in page context to access fetch() API
- Intercepts outgoing requests (user messages)
- Intercepts streaming responses (AI replies)
- Adds timestamps at API level before data reaches platform

**Popup UI:**
- Settings interface with timezone selection
- Real-time timestamp preview
- Persistent storage management

### Why API-Level Injection?

DOM manipulation breaks when platforms change UI. API-level interception:
- Survives interface redesigns
- Embeds timestamps in actual conversation data
- Works with conversation exports
- More reliable long-term

### Technical Implementation

**ClaudeClock:**
- Intercepts fetch() calls to Claude API
- Modifies request body to prepend timestamps
- Handles streaming responses via ReadableStream manipulation

**GPTClock:**
- Intercepts fetch() calls to ChatGPT API
- Modifies `content.parts[]` array in user messages
- Intercepts Server-Sent Event (SSE) streams for AI responses
- Injects timestamps into first text delta

---

## TROUBLESHOOTING

### Timestamps Not Appearing

**Solution steps:**
1. Hard refresh page: `Ctrl + Shift + R`
2. Verify extension enabled in `chrome://extensions/`
3. Check timezone configured (click extension icon)
4. Reload extension (click refresh icon on extension card)
5. Check console (F12) for "Content script loaded" message

### Extension Not Loading

**Solution steps:**
1. Verify all files present (manifest.json, content.js, injected.js, popup files, icons)
2. Check for red error text in `chrome://extensions/`
3. Verify permissions (extension needs access to claude.ai or chatgpt.com)
4. Try remove and reinstall extension

### Settings Not Saving

**Solution steps:**
1. Verify storage permission in manifest
2. Open popup UI to confirm interface works
3. Restart browser completely
4. Check console for storage-related errors

### Extension Updates Not Loading

**Solution steps:**
1. Chrome caches extension files aggressively
2. Click "Reload" on extension card in chrome://extensions/
3. If that fails, remove and reinstall extension
4. Close and reopen browser

---

## PRIVACY

**100% local processing.**

- All timestamp generation happens in browser
- No data sent to external servers (only to Claude/ChatGPT APIs as normal)
- Zero analytics, telemetry, or data collection
- Open source - inspect code yourself

Extensions only add timestamps. Your conversations remain private between you and the AI platform.

---

## LICENSE

**Apache License 2.0**

See [LICENSE](LICENSE) file for full text.

Use freely. Modify freely. Deploy freely.
Attribution appreciated but not required.

---

## CONTACT

**General Inquiries**
ops@resonantaisystems.com

**Research Collaboration**
https://resonantaicore.com

**Enterprise Partnerships**
https://resonantaisystems.com

---

*Part of the Resonant AI Systems public research toolkit. Built for AI continuity, temporal context preservation, and conversation archiving.*

---

## Individual Extension Documentation

For platform-specific details, see:
- [ClaudeClock README](ClaudeClock/README.md) - Claude.ai timestamp extension
- [GPTClock README](GPTClock/README.md) - ChatGPT timestamp extension
