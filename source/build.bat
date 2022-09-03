@echo off
python -m PyInstaller --onefile -w main.py
color 2
echo -----------------------------
echo Done Compiling!
echo You will need to move the file inside the "dist" folder to the main folder so it can read all the files.
pause