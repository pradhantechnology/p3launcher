@echo off
rem set PYTHONDONTWRITEBYTECODE=1
rem set PyAppPath=C:\Python27\pythonw.exe

rem call %PyAppPath% %~dp0main.py

rem echo %~dp0
rem pause

rem pushd %~dp0

set PYTHONDONTWRITEBYTECODE=1

rem SET PYTHONPATH=%PYTHONPATH%;%~dp0;
if exist C:\Python27 (
	echo using local python.
	set "path=C:\Python27;%path%"
) else (
	echo python27 doesnot exists.
)
rem echo %*
if exist "%~dp0\main.py" (python "%~dp0\main.py" %*)^
else pythonw "%~dp0\main.pyc" %*

rem prompt $g $c %* $f

rem echo %~dp0
rem pause
rem exit