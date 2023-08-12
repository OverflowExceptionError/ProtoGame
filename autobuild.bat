echo Auto Build Tool
pyinstaller --onefile main.py
echo Check for errors!
pause
copy dist\main.exe .
del -r -f dist
del -r -f build