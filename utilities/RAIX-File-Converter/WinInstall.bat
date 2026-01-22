@echo off
REM RAIS Document Converter - Windows Installation Script
REM This script installs all dependencies needed to run the converter

echo ================================================
echo RAIS Document Converter - Installation
echo ================================================
echo.

REM Check if Python is installed
echo [1/4] Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)
python --version
echo Python found!
echo.

REM Check if pip is available
echo [2/4] Checking pip installation...
python -m pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: pip is not available
    echo Installing pip...
    python -m ensurepip --upgrade
    if %errorlevel% neq 0 (
        echo ERROR: Failed to install pip
        pause
        exit /b 1
    )
)
python -m pip --version
echo pip found!
echo.

REM Upgrade pip to latest version
echo [3/4] Upgrading pip to latest version...
python -m pip install --upgrade pip
if %errorlevel% neq 0 (
    echo WARNING: Failed to upgrade pip, continuing anyway...
)
echo.

REM Install Python dependencies
echo [4/4] Installing Python dependencies...
echo Installing Flask, pypandoc, and xhtml2pdf...
python -m pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERROR: Failed to install dependencies
    echo Please check the error messages above
    pause
    exit /b 1
)
echo.

echo ================================================
echo Installation Complete!
echo ================================================
echo.
echo Note: Pandoc binaries will be downloaded automatically
echo on first run if not already present.
echo.
echo To start the converter, run: WinRun.bat
echo.
pause
