@echo off

reg query "hkcu\software\Python"
if ERRORLEVEL 1 GOTO NOPYTHON

:PYTHON
echo Press enter to install the WUSB Radiothon Server
pause
python Source\\setup.py develop
echo WUSB Donor Monitor server installation completed successfully!
pause
exit

:NOPYTHON
echo Cannot continue installation. Python 3.6 or greater is required to run installation.
pause
exit

