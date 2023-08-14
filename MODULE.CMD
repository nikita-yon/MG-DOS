@echo off
pip install astroid
pip install time
pip install colorama
pip install os
pip install sys
pip install wmi
pip install atexit
pip install configparser
pip install alive-progress
pip install datetime
pip install PIL
pip install playsound
pip install webbrowser
pip install keyboard
pip install operator
pip install psutil
pip install random
pip install platform
pip install re
pip install deep_translator
pip install shutil
pip install subprocess
pip install winsound
pip install threading
pip install pytimedinput

REM Проверка статуса установки модулей
if %errorlevel% equ 0 (
    echo Модули успешно установлены!
) else (
    echo Ошибка установки модулей. Проверьте, что у вас установлен Python и pip и повторите попытку.
)

pause