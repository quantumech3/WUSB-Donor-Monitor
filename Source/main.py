# -*- coding: utf-8 -*-
'''
Created by Scott Burgert on 2/17/2019
Project name: WUSB Donor Monitor ©

Module name: main.py
Module description:
        This module is what gets started when ‘start_server.sh’ is ran.
    This module starts the ‘poller.py’ module, ‘host.py’ module and the ‘cmd.py’ module.
'''


# Throw error if Python version is less then 3.6
import sys
# If python version is less then 3.x
if sys.version_info[0] < 3:
    print("WUSB Donor Monitor requires Python 3.6 or above to run.")
    # If error is thrown, that would be because it is running in python 2, so Python 2 'raw_input' is used instead of 'input'
    raw_input("Cannot continue. Press any key to exit.")
    exit(-1)
# If Python version is less then 3.6
elif sys.version_info[0] == 3 and sys.version_info[1] < 6:
    print("WUSB Donor Monitor requires Python 3.6 or above to run.")
    input("Cannot continue. Press any key to exit.")
    exit(-1)
# If Python version is greater then 3.6, throw warning
elif sys.version_info[0] > 3 or sys.version_info[1] > 6:
    print("Warning: This program was built and tested on Python 3.6 but you are running Python " + str(sys.version_info[0]) + '.' + str(sys.version_info[1]))
    print("Server will probably still work but it is recommended that you run this server on Python 3.6.")
    input("Press any key to continue...")


from time import sleep
import debug as dbg
import threading
import poller
import host
import cmd
import pickle


# Print copyright message
print("\nStarting the WUSB Donor Monitor server. This and the client-side part of this application were written and developed by Scott Burgert in 2019 (copyright) \n" +
      "-----------------------------------------------------------------------------------------------------------------------------------------------------------\n")

# Pause and give user time to read copyright message
sleep(1)

# Load config and GAPI credentials
poller.update_config_status()

# Attempt to load GAPI credentials from 'creds.pickle'
try:
    dbg.log("Attempting to load GAPI credentials file 'creds.pickle'")
    creds = pickle.load(open('creds.pickle', 'rb'))

    # Log success
    dbg.success("Successfully loaded GAPI credentials file 'creds.pickle'")

# Throw error and exit if GAPI credentials file cannot be found
except FileNotFoundError:
    dbg.err("Failed to load 'creds.pickle' because it could not be found. 'creds.pickle' is required for server to run.")
    input("Cannot continue. Press any key to exit.")
    exit(-1)

# Throw error that reads off if any other exceptions are raised
except Exception as e:
    dbg.err("Failed to load 'creds.pickle'. Got the following error instead:")
    dbg.err(str(e))
    input("Cannot continue. Press any key to exit.")
    exit(-1)

# Allocate and start poller.py module in a separate daemon thread
poller_thread = threading.Thread(target=poller.main, args=[creds])
poller_thread.setDaemon(True)
poller_thread.start()

# Print dots until poller.py has successfully initialized
print("Hold on for just a second while I get everything together")
while poller.radiothonInfo == {}:
    print(".")
    sleep(1)

# Allocate and start host.py module in a seperate daemon thread
host_thread = threading.Thread(target=host.main)
host_thread.setDaemon(True)
host_thread.start()

# Give time for host_thread to start so host.py module logs don't interfere with cmd line logs
sleep(0.5)

# Log success
print('\n' * 3)
print('Success! Server is running on port 80')

# Start cmd.py module in main thread
cmd.main()
