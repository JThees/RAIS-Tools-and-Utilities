<div align="center">

# Resonant AI Systems TOOLS & UTILITIES

## AIParley

### Built by Resonant AI Core
**Research & Development Division of Resonant AI Systems**

![License](https://img.shields.io/badge/license-Apache%202.0-blue)
![Status](https://img.shields.io/badge/status-active%20development-brightgreen)
![Scope](https://img.shields.io/badge/scope-research%20tool-purple)
![Division](https://img.shields.io/badge/division-Resonant%20AI%20Core-black)

**Automated relay system for multi-platform AI interaction.**

Browser extension that relays conversations between Claude.ai and ChatGPT.com. Enables systematic study of multi-agent collaboration, conversation dynamics, and comparative AI behavior under controlled research conditions.
Not a chatbot. Not a wrapper. **Direct platform integration for behavioral research.**

</div>

---

## WHAT THIS IS

AIParley automates message relay between Claude.ai and ChatGPT.com, creating controlled research environments for multi-agent AI interaction.

**Core functionality:**
- Bidirectional message relay between Claude ↔ ChatGPT
- Natural timing simulation with configurable delays
- Comprehensive conversation logging and export
- Session management with approval gates and emergency stops
- Optional WebSocket server for multi-browser coordination

This is a research tool. It enables systematic observation of how different AI architectures communicate, collaborate on problems, and handle turn-taking dynamics.

---

## WHY IT EXISTS

Studying multi-agent AI behavior requires repeatable, controlled environments. Manual relay is slow and introduces human bias. AIParley automates the mechanical work while preserving operator oversight.

**Research use cases:**
- Comparative architecture studies (different model families in dialogue)
- Collaborative problem-solving dynamics
- Communication pattern analysis across AI systems
- Educational demonstrations of multi-agent coordination

Built for researchers who need automated relay without losing control over the research protocol.

---

## FEATURES

### Core Capabilities
- **Platform integration** - Chrome/Edge extension with CSS selector-based DOM interaction
- **Configurable timing** - Delay ranges, natural variance, rate limiting for platform compliance
- **Session controls** - Manual approval mode, emergency stop, health checks
- **Conversation export** - JSON (full metadata), CSV (analysis-ready), TXT (readable archive)

### Advanced Options
- **WebSocket relay** - Coordinate sessions across multiple browsers
- **Trigger customization** - Configure activation phrases and platform selectors
- **Statistics dashboard** - Session metrics, message counts, timing analysis
- **Multi-session management** - Track and resume research sessions

---

## REQUIREMENTS

**Runtime:**
- Chrome or Edge browser (Manifest V3 support)
- Active accounts on target AI platforms (Claude.ai, ChatGPT.com)

**Development:**
- Git (for repository clone)
- Text editor (for configuration customization)

**Optional:**
- Node.js (for WebSocket server in multi-browser mode)

---

## INSTALLATION

### Basic Setup

1. **Clone repository**
   ```bash
   git clone https://github.com/resonantaisystems/RAIS-Tools-and-Utilities.git
   cd RAIS-Tools-and-Utilities/utilities/aiparley
   ```

2. **Load extension**
   - Open `chrome://extensions/` (or `edge://extensions/`)
   - Enable "Developer mode" (toggle in top-right)
   - Click "Load unpacked"
   - Select the `aiparley` directory

3. **Verify installation**
   - AIParley icon appears in browser toolbar
   - Click icon to open control popup
   - Run health check to verify platform detection

### Advanced Setup (Multi-Browser)

For coordination across browsers or remote relay:

```bash
cd websocket-server
npm install
node server.js
```

Configure WebSocket endpoint in extension options. See [MultiBrowser.md](MultiBrowser.md) for details.

---

## USAGE

### Starting a Research Session

1. **Prepare platforms**
   - Open Claude.ai in one tab
   - Open ChatGPT.com in another tab
   - Ensure both platforms are logged in and responsive

2. **Configure session**
   - Click AIParley icon in toolbar
   - Set research topic/initial prompt
   - Configure timing (delay range, session length)
   - Choose approval mode (auto-relay or manual approval)

3. **Run health check**
   - Click "Health Check" in popup
   - Verify both platforms detected correctly
   - Check DOM selectors if detection fails

4. **Start relay**
   - Click "Start Session"
   - First message sent to configured starting platform
   - Automatic relay begins (respecting approval settings)

5. **Monitor and control**
   - Watch statistics in popup dashboard
   - Use emergency stop if needed
   - Approve messages manually if in approval mode

6. **Export results**
   - Click "Export Session" when complete
   - Choose format (JSON for analysis, TXT for archive)
   - Save conversation data locally

### Example Research Protocol

**Topic:** "Design a local-first note-taking application"

**Configuration:**
- Delay range: 20-35 seconds
- Session length: 15 exchanges
- Mode: Manual approval
- Starting platform: Claude

**Process:**
1. Initial prompt sent to Claude
2. AIParley waits for Claude's response
3. Response captured and queued for ChatGPT
4. Operator approves relay (manual mode)
5. Message sent to ChatGPT after configured delay
6. Cycle repeats for configured exchange count
7. Export conversation for analysis

---

## STATUS & ROADMAP

**Current Status:** Active Development

AIParley is functional and used in active research. Core relay mechanisms are stable. Platform selectors require updates when Claude.ai or ChatGPT.com change their DOM structure.

**Known Issues:**
- Platform UI updates break DOM selectors (requires manual configuration update)
- Rate limiting varies by platform (adjust delays if relay fails)
- Browser must remain active (no background tab support yet)

**Roadmap:**
- **Selector auto-detection** - Reduce manual configuration when platforms update
- **Additional platform support** - Gemini, Perplexity, local LLMs via API
- **Enhanced export formats** - Markdown with metadata, graph data for network analysis
- **Background operation** - Service worker improvements for inactive tab handling

**Maintenance:** Active. Platform selector updates pushed as needed.

---

## RESEARCH ETHICS

**This tool requires ethical use.**

### Appropriate Uses
- Academic research with institutional approval
- Comparative AI behavior studies
- Educational demonstrations
- Personal experimentation within platform terms

### Requirements
- Comply with Claude.ai and ChatGPT.com terms of service
- Respect rate limits and platform resources
- Obtain necessary research approvals for publication
- Do not use for automated spam, content generation at scale, or platform abuse

### Rate Limiting
AIParley enforces minimum delays to prevent platform overload. Default settings respect platform guidelines. Adjust only within ethical bounds.

---

## DOCUMENTATION

Additional documentation in this directory:

- [QUICKSTART.md](QUICKSTART.md) - Step-by-step first session guide
- [INSTALLATION.md](INSTALLATION.md) - Detailed setup for all environments
- [MultiBrowser.md](MultiBrowser.md) - WebSocket server configuration
- [DEBUGGING.md](DEBUGGING.md) - Troubleshooting platform selector issues
- [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) - Architecture and development notes

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

*Part of the Resonant AI Systems public research toolkit. Built for AI continuity, sovereign architectures, and operator-controlled multi-agent systems.*
