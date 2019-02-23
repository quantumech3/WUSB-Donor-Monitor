# -*- coding: utf-8 -*-
'''
Created by Scott Burgert on 2/23/2019
Project name: WUSB Donor Monitor ©

Module name: cmd.py
Module description:
        This module runs on the main thread after startup has completed.
        This module has an entry point that is called by the ‘main.py’ module.
        This module provides a text based user interface on server side.
'''

from time import sleep
import poller
import host

def exit_cmd():
    '''
    Exit command
    :return: None
    '''

    # Get input from user as string (input() sometimes auto-casts which could cause an error)
    inpt = str(input("Are you sure you want to exit? (‘yes’ or ‘no’) \n"))

    # Make input lowercase so 'COMMAND' is the same as 'command'
    inpt = inpt.lower()

    # Quit if input is yes
    if inpt == 'yes':
        # Print friendly message :)
        print("Ok. Bye bye!")
        # Pause for 2 seconds so user can read friendly message
        sleep(1)
        # Stop program
        quit(0)
    # Else if user entered 'no'
    elif inpt == 'no':
        print("Ok, i’ll continue doing server stuff… Beep boop!")
    # Ask user again if he/she wants to quit again if she enters nonsence
    else:
        unknown_cmd()
        exit_cmd()

def refresh_cmd():
    '''
    Refresh command
    '''

    # Tell user that Radiothon information is being updated
    print("Reading new Radiothon information from Google Sheets and config file...")

    # Get copy of radiothonInfo to compare against
    _radiothonInfo = poller.radiothonInfo

    # Update radiothonInfo state
    poller.update_radiothonInfo()

    # Tell user that new information is being sent to clients
    print("Sending new Radiothon information to clients...")

    # Emit pageData event
    host.emit_pageData()

    # Log success
    print("Successfully refreshed!")

def unknown_cmd():
    print("What does that mean? I don’t understand that!")

def main():
    '''
    Entry point for cmd.py module
    '''

    # Prompt user for input continuously
    while True:
        # Get input from user as string (input() sometimes auto-casts which could cause an error)
        inpt = str(input("RADIOTHON_CONSOLE[]: "))

        # Make input lowercase so 'COMMAND' is the same as 'command'
        inpt = inpt.lower()

        # Execute command the user inputs
        if inpt == 'exit':
            exit_cmd()
        elif inpt == 'refresh':
            refresh_cmd()
        elif inpt != '':
            unknown_cmd()  # Run default 'unknown' command if user entered something (not a blank string)
