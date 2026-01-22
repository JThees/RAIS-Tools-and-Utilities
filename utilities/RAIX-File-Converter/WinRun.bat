@echo off
REM RAIS Document Converter - Windows Run Script
REM This script launches the Flask server

echo ================================================
echo RAIS Document Converter
echo ================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please run WinInstall.bat first
    pause
    exit /b 1
)

REM Check if Flask is installed
python -c "import flask" >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Flask is not installed
    echo Please run WinInstall.bat first
    pause
    exit /b 1
)

echo Starting RAIS Document Converter...
echo Server will be available at: http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo ================================================
echo.

REM Run the Flask application
python app.py

REM If the server stops, pause so user can see any error messages
if %errorlevel% neq 0 (
    echo.
    echo ================================================
    echo Server stopped with errors
    echo ================================================
    pause
)
