# Text Cleaner

**Clean and Process Text Files with Advanced Phrase Stripping**

A cross-platform desktop application for processing text files by removing whitespace, custom phrases, and extracting specific content.

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Stable-green.svg)]()
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)]()

---

## What Is This?

Text Cleaner is a powerful desktop application built with Python and Tkinter that provides:

- **Whitespace removal** - Strip all extra spaces, tabs, and line breaks
- **Phrase stripping** - Remove custom phrases and signatures permanently
- **Content extraction** - Save the last N lines to a new file
- **File appending** - Append processed content to existing files
- **Persistent settings** - Remember your preferences between sessions
- **Dark theme interface** - Clean, modern UI with dark styling

Part of **RAIS Tools and Utilities** collection.

---

## Current Status

**Phase: Stable Release**

✅ **Completed:**
- Cross-platform desktop application
- Dark-themed user interface
- Phrase stripping with persistent storage
- Whitespace removal algorithms
- File processing capabilities
- Configuration persistence

⏳ **In Progress:**
- User experience refinements
- Additional file format support

❌ **Not Started:**
- Command-line interface
- Batch processing mode
- Advanced regex patterns

---

## Features

### Core Functionality
- **Text Processing** - Remove all whitespace from text and markdown files
- **Phrase Management** - Strip custom phrases stored in `phrases.txt`
- **Content Extraction** - Extract and save the last N lines to new files
- **File Operations** - Append processed text to existing files

### User Interface
- **Dark Theme** - Modern, easy-on-the-eyes interface
- **File Selection** - Browse dialogs with all file type support
- **Persistent Settings** - Line count and preferences remembered
- **Real-time Feedback** - Success/error messages for all operations

### Cross-Platform Support
- **Windows 10+** - Full compatibility
- **Linux** - Arch, Ubuntu, and other distributions
- **macOS** - Modern versions supported

---

## Requirements

- **Python 3.6+** - Core runtime environment
- **Tkinter** - GUI framework (included with Python)
- **Standard libraries** - `os`, `re`, `tkinter`, `filedialog`

---

## Installation

1. **Clone or download** this repository
2. **Navigate** to the project directory
3. **Install dependencies** (optional, as Tkinter is included):
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the application**:
   ```bash
   python text_cleaner.py
   ```

---

## Usage

### Basic Operation
1. **Select Source File** - Click "Browse..." to choose input file
2. **Configure Options** - Choose append or extract operations
3. **Set Phrase Stripping** - Edit phrases in `phrases.txt` or the UI field
4. **Process File** - Click "Process File" to execute

### Advanced Features
- **Phrase Persistence** - Add phrases to `phrases.txt` for permanent storage
- **Line Count Memory** - Your preferred N value is saved automatically
- **File Type Flexibility** - Supports .txt, .md, and all file types
- **Overwrite Protection** - Optional file overwrite for output files

---

## Building Executables

Create standalone executables for distribution:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed text_cleaner.py
```

This creates platform-specific executables in the `dist/` folder.

---

## Configuration Files

- **`phrases.txt`** - Permanent phrase storage for stripping
- **`config.txt`** - User preferences and settings
- **`requirements.txt`** - Python dependencies

---

## License

Apache 2.0 - See LICENSE file

---

## Links

**[Resonant AI Systems](https://resonantaisystems.com)** | **[Sovereign AI Collective](https://github.com/ResonantAISystems/Continuity-Project)**
