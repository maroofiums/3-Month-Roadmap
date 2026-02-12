@echo off
echo Starting Velox Demo Server...
echo.

REM Get the directory where this batch file is located
set "PROJECT_DIR=%~dp0"

REM Add project to Python path and run
set PYTHONPATH=%PROJECT_DIR%;%PYTHONPATH%

REM Change to demo directory
cd "%PROJECT_DIR%demo"

REM Run the server
python -c "import sys; sys.path.insert(0, r'%PROJECT_DIR%'); exec(open(r'%PROJECT_DIR%demo\main.py').read())"

pause
