@echo off
cd /d %~dp0

python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python and try again.
    pause
    exit /b
)

echo Installing required packages...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo Starting OTP sender...
python main.py

pause
