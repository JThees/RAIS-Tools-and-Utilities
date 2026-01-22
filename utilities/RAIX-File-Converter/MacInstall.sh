#!/bin/bash
# RAIS Document Converter - macOS Installation Script
# This script installs all dependencies needed to run the converter

set -e  # Exit on error

echo "================================================"
echo "RAIS Document Converter - macOS Installation"
echo "================================================"
echo ""

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Determine Python command (python3 or python)
PYTHON_CMD=""
if command_exists python3; then
    PYTHON_CMD="python3"
elif command_exists python; then
    PYTHON_CMD="python"
else
    echo "ERROR: Python is not installed"
    echo ""
    echo "Please install Python 3.8+ using one of these methods:"
    echo "  1. Download from: https://www.python.org/downloads/"
    echo "  2. Install via Homebrew: brew install python3"
    echo "  3. Install via MacPorts: sudo port install python311"
    echo ""
    exit 1
fi

# Verify Python version is 3.8+
echo "[1/5] Checking Python installation..."
PYTHON_VERSION=$($PYTHON_CMD --version 2>&1 | awk '{print $2}')
echo "Found: Python $PYTHON_VERSION"

# Check if version is at least 3.8
MAJOR=$($PYTHON_CMD -c 'import sys; print(sys.version_info.major)')
MINOR=$($PYTHON_CMD -c 'import sys; print(sys.version_info.minor)')

if [ "$MAJOR" -lt 3 ] || ([ "$MAJOR" -eq 3 ] && [ "$MINOR" -lt 8 ]); then
    echo "ERROR: Python 3.8 or higher is required"
    echo "Current version: $PYTHON_VERSION"
    exit 1
fi
echo "Python version OK!"
echo ""

# Determine pip command
echo "[2/5] Checking pip installation..."
PIP_CMD=""
if command_exists pip3; then
    PIP_CMD="pip3"
elif command_exists pip; then
    PIP_CMD="pip"
else
    echo "pip not found, attempting to install..."
    $PYTHON_CMD -m ensurepip --upgrade
    if command_exists pip3; then
        PIP_CMD="pip3"
    elif command_exists pip; then
        PIP_CMD="pip"
    else
        PIP_CMD="$PYTHON_CMD -m pip"
    fi
fi

$PIP_CMD --version
echo "pip found!"
echo ""

# Upgrade pip
echo "[3/5] Upgrading pip to latest version..."
$PYTHON_CMD -m pip install --upgrade pip || echo "Warning: Could not upgrade pip, continuing..."
echo ""

# Install virtualenv (optional but recommended)
echo "[4/5] Checking for virtualenv (optional)..."
if ! $PYTHON_CMD -c "import venv" >/dev/null 2>&1; then
    echo "Note: venv module not available, installing..."
    $PIP_CMD install virtualenv || echo "Could not install virtualenv, continuing..."
fi
echo ""

# Install dependencies
echo "[5/5] Installing Python dependencies..."
echo "Installing Flask, pypandoc, and xhtml2pdf..."
$PIP_CMD install -r requirements.txt

if [ $? -ne 0 ]; then
    echo ""
    echo "ERROR: Failed to install dependencies"
    echo "Trying with --user flag..."
    $PIP_CMD install --user -r requirements.txt

    if [ $? -ne 0 ]; then
        echo "ERROR: Installation failed"
        echo "Please check the error messages above"
        exit 1
    fi
fi
echo ""

# Make run script executable
if [ -f "MacRun.sh" ]; then
    chmod +x MacRun.sh
    echo "MacRun.sh is now executable"
fi

echo "================================================"
echo "Installation Complete!"
echo "================================================"
echo ""
echo "Note: Pandoc binaries will be downloaded automatically"
echo "on first run if not already present."
echo ""
echo "To start the converter, run: ./MacRun.sh"
echo ""
