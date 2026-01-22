#!/bin/bash
# RAIS Document Converter - Arch Linux Installation Script
# This script installs all dependencies needed to run the converter

set -e  # Exit on error

echo "================================================"
echo "RAIS Document Converter - Arch Linux Installation"
echo "================================================"
echo ""

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check if running as root (not recommended for pip installs)
if [ "$EUID" -eq 0 ]; then
    echo "WARNING: Running as root is not recommended"
    echo "Consider running as a regular user"
    echo ""
fi

# Determine Python command
PYTHON_CMD=""
if command_exists python; then
    PYTHON_CMD="python"
elif command_exists python3; then
    PYTHON_CMD="python3"
else
    echo "ERROR: Python is not installed"
    echo ""
    echo "Install Python using one of these commands:"
    echo "  sudo pacman -S python python-pip"
    echo ""
    read -p "Would you like to install Python now? (y/N) " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        sudo pacman -S --needed python python-pip
        if command_exists python; then
            PYTHON_CMD="python"
        elif command_exists python3; then
            PYTHON_CMD="python3"
        else
            echo "ERROR: Installation failed"
            exit 1
        fi
    else
        exit 1
    fi
fi

# Verify Python version
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

# Check for pip
echo "[2/5] Checking pip installation..."
PIP_CMD=""
if command_exists pip; then
    PIP_CMD="pip"
elif command_exists pip3; then
    PIP_CMD="pip3"
else
    echo "pip not found, attempting to install..."
    echo "Installing pip via pacman..."
    sudo pacman -S --needed python-pip

    if command_exists pip; then
        PIP_CMD="pip"
    elif command_exists pip3; then
        PIP_CMD="pip3"
    else
        # Try using python -m pip
        PIP_CMD="$PYTHON_CMD -m pip"
    fi
fi

$PIP_CMD --version
echo "pip found!"
echo ""

# Upgrade pip
echo "[3/5] Upgrading pip to latest version..."
$PYTHON_CMD -m pip install --upgrade pip --user || echo "Warning: Could not upgrade pip, continuing..."
echo ""

# Check for optional system dependencies
echo "[4/5] Checking optional system dependencies..."

# Check if wkhtmltopdf is available (alternative PDF renderer)
if ! command_exists wkhtmltopdf; then
    echo "Note: wkhtmltopdf not found (optional)"
    echo "Install with: sudo pacman -S wkhtmltopdf"
fi

# Check if pandoc is in repos (user might want system version)
if ! command_exists pandoc; then
    echo "Note: pandoc not found (will be downloaded automatically by pypandoc)"
    echo "Alternatively install system package: sudo pacman -S pandoc"
else
    echo "Found system pandoc: $(pandoc --version | head -n1)"
fi
echo ""

# Install Python dependencies
echo "[5/5] Installing Python dependencies..."
echo "Installing Flask, pypandoc, and xhtml2pdf..."

# Try regular install first
$PIP_CMD install -r requirements.txt

if [ $? -ne 0 ]; then
    echo ""
    echo "Regular installation failed, trying with --user flag..."
    $PIP_CMD install --user -r requirements.txt

    if [ $? -ne 0 ]; then
        echo ""
        echo "ERROR: Installation failed"
        echo ""
        echo "Troubleshooting steps:"
        echo "  1. Make sure you have base-devel installed: sudo pacman -S base-devel"
        echo "  2. Try installing in a virtual environment:"
        echo "     python -m venv venv"
        echo "     source venv/bin/activate"
        echo "     pip install -r requirements.txt"
        echo ""
        exit 1
    fi

    # Add user bin to PATH reminder
    echo ""
    echo "Note: Packages installed with --user flag"
    echo "If you get 'command not found' errors, add this to your ~/.bashrc:"
    echo "  export PATH=\"\$HOME/.local/bin:\$PATH\""
    echo ""
fi

# Make run script executable
if [ -f "ArchRun.sh" ]; then
    chmod +x ArchRun.sh
    echo "ArchRun.sh is now executable"
fi

echo ""
echo "================================================"
echo "Installation Complete!"
echo "================================================"
echo ""
echo "Note: Pandoc binaries will be downloaded automatically"
echo "on first run if not already present."
echo ""
echo "To start the converter, run: ./ArchRun.sh"
echo ""
