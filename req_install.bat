@echo off
start cmd /k pip install -r requirements.txt
pause
start cmd /k python.exe -m pip install --upgrade pip
break
