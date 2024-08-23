@echo off
REM Compile the Python scripts
pyinstaller --onefile --noconsole .\OpenBrowser.py
pyinstaller --onefile --noconsole --hidden-import=winshell .\OpenBrowserGUI.py

REM Move out the compiled executables
move .\dist\OpenBrowser.exe .\OpenBrowser.exe
move .\dist\OpenBrowserGUI.exe .\OpenBrowserGUI.exe

echo Release created.
pause
