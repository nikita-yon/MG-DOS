@echo off
setlocal enabledelayedexpansion

REM Проверяем, установлен ли pip
python -m pip --version
IF %ERRORLEVEL% NEQ 0 (
    echo "Error: pip is not installed."
    echo "Please install pip first and then run this script again."
    pause
    exit /b 1
)

REM Устанавливаем необходимые модули
pip install colorama
pip install configparser
pip install alive-progress
pip install pillow
pip install playsound
pip install keyboard
pip install psutil
pip install deep_translator

echo "Modules installation completed."
pause
