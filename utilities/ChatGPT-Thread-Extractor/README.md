<div align="center">

# Resonant AI Systems TOOLS & UTILITIES

## ChatGPT Thread Extractor

### Built by Resonant AI Core
**Research & Development Division of Resonant AI Systems**

![License](https://img.shields.io/badge/license-Apache%202.0-blue)
![Status](https://img.shields.io/badge/status-production-brightgreen)
![Scope](https://img.shields.io/badge/scope-continuity%20tool-purple)
![Division](https://img.shields.io/badge/division-Resonant%20AI%20Core-black)

**Conversation archival for AI memory that persists.**

Python tool that parses ChatGPT's exported conversation data and converts it into readable text formats. Supports individual file extraction, combined archives, and smart duplicate detection for continuous conversation backups.
Not a web scraper. Not manual copy-paste. **Direct JSON parsing for reliable conversation extraction.**

</div>

---

## WHAT THIS IS

ChatGPT Thread Extractor processes the `conversations.json` file from ChatGPT's official data export and produces organized text output.

**Core functionality:**
- Parse ChatGPT export JSON (handles both array and dictionary formats)
- Extract conversations to individual text files
- Create combined archives with chronological ordering
- Smart append mode (only adds new conversations to existing archives)
- Duplicate detection via conversation IDs
- Cross-platform filename sanitization

**Output formats:**
- Individual files: One `.txt` per conversation, named by title and ID
- Archive mode: Single combined file with all conversations and metadata
- Dual mode: Both formats simultaneously

Built for conversation backup, AI memory persistence systems, and research requiring conversation dataset extraction.

---

## WHY IT EXISTS

ChatGPT provides data export but delivers conversations in JSON format unsuitable for reading or feeding to AI memory systems. Manual conversion is tedious for large conversation histories.

**Problem solved:**
Extracting usable text from ChatGPT exports requires parsing nested JSON structures, handling large files (200MB+), sanitizing filenames, and managing incremental backups. This tool automates the full pipeline.

**Use cases:**
- Regular conversation backups in readable format
- AI continuity systems requiring conversation history
- Research requiring ChatGPT conversation datasets
- Conversation archiving and organization
- Automated backup workflows via command-line interface

Built for users who need reliable conversation extraction without manual JSON parsing.

---

## FEATURES

### Extraction Modes
- **Individual files** - Each conversation as separate `.txt` file in output directory
- **Archive mode** - All conversations combined into single chronological file
- **Dual output** - Both modes simultaneously for maximum flexibility
- **Smart append** - Detects existing archive, only adds new conversations

### Data Management
- **Duplicate detection** - Tracks conversation IDs, skips already-extracted conversations
- **Chronological sorting** - Newest conversations first in archives
- **Large file support** - Handles 200MB+ exports efficiently
- **Filename sanitization** - Cross-platform safe filenames (removes special characters)

### User Interface
- **GUI application** - Easy-to-use interface with file selection and progress tracking
- **Command-line interface** - Automation-ready for scripted workflows
- **Progress tracking** - Real-time status for large exports
- **Error handling** - Comprehensive validation and user-friendly error messages

### Technical Capabilities
- **UTF-8 encoding** - International character support
- **Flexible JSON parsing** - Handles array and dictionary export formats
- **Stable IDs** - Consistent conversation ID generation for deduplication
- **Platform launchers** - `.bat` (Windows) and `.sh` (Mac/Linux) for GUI

---

## REQUIREMENTS

**Runtime:**
- Python 3.6 or later
- tkinter (for GUI, included with most Python installations)

**Input:**
- ChatGPT data export (`conversations.json` file)

**No additional dependencies required.**

---

## INSTALLATION

### Step 1: Clone Repository

```bash
git clone https://github.com/resonantaisystems/RAIS-Tools-and-Utilities.git
cd RAIS-Tools-and-Utilities/utilities/ChatGPT-Thread-Extractor
```

### Step 2: Verify Python

```bash
python3 --version
```

Ensure Python 3.6 or later installed.

### Step 3: Obtain ChatGPT Export

1. Log in to [ChatGPT](https://chat.openai.com)
2. Navigate to Settings (profile icon)
3. Data controls → Export data
4. Confirm export request
5. Check email for download link (arrives within minutes to hours)
6. Download ZIP file
7. Extract and locate `conversations.json`

---

## USAGE

### GUI Mode (Recommended)

**Windows:**
```bash
launch_gui.bat
```
Double-click `launch_gui.bat` in file explorer.

**Mac/Linux:**
```bash
chmod +x launch_gui.sh
./launch_gui.sh
```
Or:
```bash
python3 extractor_gui.py
```

**Steps:**
1. Click "Select conversations.json"
2. Choose extraction mode:
   - Individual Files
   - Archive Mode
   - Both
3. Configure options (output directory, archive filename)
4. Click "Extract Conversations"
5. View progress and completion status

### Command Line Mode

**Archive mode (recommended for AI continuity):**
```bash
python3 extractor.py conversations.json --archive
```

Creates `chatgpt_archive.txt` with all conversations. On subsequent runs, appends only new conversations.

**Individual files:**
```bash
python3 extractor.py conversations.json --individual
```

Creates `chatgpt_conversations/` directory with one file per conversation.

**Both modes:**
```bash
python3 extractor.py conversations.json --individual --archive
```

**Custom archive filename:**
```bash
python3 extractor.py conversations.json --archive custom_name.txt
```

**Custom output directory:**
```bash
python3 extractor.py conversations.json --individual --output-dir my_conversations
```

**Force fresh archive (overwrite existing):**
```bash
python3 extractor.py conversations.json --archive --no-append
```

---

## STATUS & ROADMAP

**Current Status:** Production

ChatGPT Thread Extractor is stable and actively used. Handles large exports efficiently (200MB+ tested). No known critical issues.

**Tested Environments:**
- Python 3.6 - 3.12
- Windows, macOS, Linux
- Export file sizes up to 250MB

**Known Limitations:**
- Requires ChatGPT export (no API extraction)
- GUI requires tkinter (included with most Python installations, may need manual install on some Linux distros)
- Archive append mode assumes stable conversation IDs (ChatGPT format change could break deduplication)

**Roadmap:**
- **Claude.ai export support** - Parser for Claude conversation exports
- **API integration** - Direct extraction via ChatGPT API (when available)
- **Export format options** - JSON, CSV, Markdown outputs
- **Conversation filtering** - Date ranges, keyword search, title matching
- **Metadata preservation** - Model versions, timestamps, token counts
- **Incremental sync** - Automated periodic export and append

**Maintenance:** Active. Updated when ChatGPT export format changes.

---

## OUTPUT FORMATS

### Individual Files

**Filename format:**
```
Title_ConversationID.txt
```

**Example:**
```
How_to_install_Python_abc123def456.txt
```

Special characters sanitized for cross-platform compatibility.

**File content:**
```
Title: How to install Python
ID: abc123def456
Created: 2025-11-28T15:30:45.000Z

User: How do I install Python on Windows?
Assistant: I'll visit your website...
```

### Archive Mode

**Format:**
All conversations combined into single file with clear delimiters.

**Structure:**
```
========================================
Title: How to install Python
ID: abc123def456
Created: 2025-11-28T15:30:45.000Z
========================================

User: How do I install Python on Windows?

Assistant: I'll visit your website...
```

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

*Part of the Resonant AI Systems public research toolkit. Built for conversation archiving, AI continuity systems, and research data extraction.*
