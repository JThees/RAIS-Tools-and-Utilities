/*
 * =================================================================================
 * RAIC (Resonant AI Core) - Community Tools
 * =================================================================================
 * 
 * Part of the RAIC open-source toolkit for AI sovereign research and development.
 * 
 * Copyright 2025 Resonant AI Systems
 * 
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 * 
 *     http://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * 
 * =================================================================================
 * [For more information about RAIC:](https://resonantaicore.com/)
 * =================================================================================
 */    

## Overview

AIParley facilitates controlled research environments for studying how different AI systems communicate and collaborate. The tool enables researchers to study conversation dynamics, collaborative problem-solving, and multi-agent AI behavior patterns by automatically relaying messages between AI platforms with natural timing patterns.

**Current Status:** Beta - Active development  
**Supported Platforms:** Claude.ai, ChatGPT.com

---

## Key Features

**Research Capabilities**
- Multi-platform AI communication relay (Claude ↔ ChatGPT)
- Natural timing simulation with configurable delays
- Comprehensive conversation logging and export
- Session management with configurable parameters

**Safety & Control**
- Manual approval mode for message review
- Emergency stop functionality
- Rate limiting and platform compliance
- Health check system for platform verification

**Advanced Options**
- Multi-browser support via WebSocket
- Multiple export formats (JSON, CSV, TXT)
- Configurable trigger phrases and selectors
- Statistics dashboard and session tracking

---

## Quick Start

### Installation

1. **Download the extension**
   ```bash
   git clone https://github.com/your-repo/aiparley.git
   cd aiparley
   ```

2. **Load in Chrome/Edge**
   - Navigate to `chrome://extensions/`
   - Enable "Developer mode"
   - Click "Load unpacked" and select the `AIParley` folder

3. **Verify installation**
   - Look for AIParley icon in toolbar
   - Click to access control popup

### Basic Research Session

1. **Prepare platforms** - Open Claude.ai and ChatGPT.com in separate tabs
2. **Configure session** - Set topic and parameters via extension popup
3. **Run health check** - Verify platform detection
4. **Start research** - Click "Start Session" to begin automated relay
5. **Export results** - Save conversation data when complete

---

## Configuration

**Timing Settings**
- Message delays: 15-30 seconds (configurable)
- Session length: 10-20 exchanges (configurable)
- Rate limiting: 10 second minimum delay

**Trigger Phrases** (Default)
- `Hey Claude`
- `Hey ChatGPT`
- `Hey Assistant`

**Export Formats**
- JSON (detailed metadata)
- CSV (spreadsheet compatible)
- TXT (human readable)

---

## Research Ethics

**Appropriate Research Uses:**
- Academic study of AI communication patterns
- Analysis of collaborative problem-solving dynamics
- Comparative AI architecture research
- Educational demonstrations

**Requirements:**
- Comply with platform terms of service
- Use reasonable rate limits
- Obtain necessary research approvals
- Report findings ethically

---

## Technical Details

**Requirements:** Chrome/Edge browser with developer mode  
**Architecture:** Manifest V3 extension with optional WebSocket server  
**Platform Integration:** CSS selector-based DOM interaction  

For detailed configuration, troubleshooting, and development information, see the [full documentation](docs/).

---

## License

Licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for details.

---

*This tool is designed for legitimate academic research and requires compliance with AI platform terms of service.*