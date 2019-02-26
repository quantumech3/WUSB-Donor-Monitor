# -*- coding: utf-8 -*-
'''
Created by Scott Burgert on 2/17/2019
Project name: WUSB Donor Monitor ©

Module name: setup.py
Module description:
        Install script that either gets invoked by 'install_windows.bat' or 'install_linux.sh'
'''


from setuptools import setup

setup(
    name='WUSB-Server',
    version='1.0',
    packages=[''],
    url='',
    license='Copyright',
    author='Scott Burgert',
    author_email='quantumech3@gmail.com',
    description='People who help run the WUSB Radiothon currently don\'t have an easy and accessible way to efficiently view information about the WUSB Radiothon. This program allows anyone working for WUSB to get near real time access to current information regarding a Radiothon.',
    install_requires=['gspread', 'oauth2client', 'Flask', 'eventlet', 'Flask-SocketIO']
)
