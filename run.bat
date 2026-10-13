@echo off
rem LM Studio Chinese patch launcher
rem Requires Python 3.8+ (python.org installer with "py" launcher or PATH enabled)

py -3 "%~dp0lmstudio_chinese_patch.py" %*
if not errorlevel 9009 goto :end

python "%~dp0lmstudio_chinese_patch.py" %*
if not errorlevel 9009 goto :end

echo [ERROR] Python not found. Please install Python 3.8+ from https://www.python.org/downloads/
echo         Remember to check "Add python.exe to PATH" during installation.

:end
pause
