#!/bin/bash
# RAIS Document Converter - macOS Run Script
# This script launches the Flask server

echo "================================================"
echo "RAIS Document Converter"
echo "================================================"
echo ""

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Determine Python command
PYTHON_CMD=""
if command_exists python3; then
    PYTHON_CMD="python3"
elif command_exists python; then
    PYTHON_CMD="python"
else
    echo "ERROR: Python is not installed"
    echo "Please run ./MacInstall.sh first"
    exit 1
fi

# Check if Flask is installed
if ! $PYTHON_CMD -c "import flask" >/dev/null 2>&1; then
    echo "ERROR: Flask is not installed"
    echo "Please run ./MacInstall.sh first"
    exit 1
fi

# Check if app.py exists
if [ ! -f "app.py" ]; then
    echo "ERROR: app.py not found"
    echo "Please make sure you're running this script from the project directory"
    exit 1
fi

echo "Starting RAIS Document Converter..."
echo "Server will be available at: http://localhost:5000"
echo ""
echo "Press Ctrl+C to stop the server"
echo "================================================"
echo ""

# Run the Flask application
$PYTHON_CMD app.py

# Capture exit code
EXIT_CODE=$?

if [ $EXIT_CODE -ne 0 ] && [ $EXIT_CODE -ne 130 ]; then
    echo ""
    echo "================================================"
    echo "Server stopped with errors (Exit code: $EXIT_CODE)"
    echo "================================================"
fi
