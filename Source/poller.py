# -*- coding: utf-8 -*-
'''
Created by Scott Burgert on 2/20/2019
Project name: WUSB Donor Monitor ©

Module name: poller.py
Module description:
        This module runs on an independant daemon thread.
        This module has an entry point that is called by the ‘main.py’ module.
        This module’s purpose is to get up-to-date GSheets donor information on a certain interval.
        The data gotten from GSheets is globally accessible by every other module.
'''

import gsparser
from database import Database
from time import sleep
import threading
import debug as dbg
import json

# This variable gets set by the command line module when ‘reload’ command is called and on startup.
# This variable is a ‘server_config’ data structure.
config = {}

# This variable gets linked with a donor entry document when entry point is called.
# Used to access data from GSheets.
database = Database

# This variable contains information that is sent to client as a ‘RadiothonInfo’ data structure
radiothonInfo = {}


def update_radiothonInfo():
    '''
    This method updates the global ‘radiothonInfo’ variable by getting the latest data from GSheets document and
    parsing it and the config into a ‘RadiothonInfo’ data structure.
    This method uses the ‘gsparser.py’ module to process all the data.

    :return: None
    '''

    # Bring global variables into local scope
    global radiothonInfo
    global database
    global config

    # Update config
    dbg.log("Attempting to update server config status")
    update_config_status()

    # Log success
    dbg.success("Server config status successfully updated")

    # Log radiothonInfo update attempt
    dbg.log("Attempting to update server status (poller.radiothonInfo)")

    # Get header from GSheets doc to compare pledges against
    header = database.get_row(0)
    # PledgeDict accumulator
    pledges = []
    # Get all rows with content from GSheets doc and turn them into PledgeDict's
    # Iterate through all rows and break at the first empty one
    for i in range(1, 1000):
        # Get row
        row = database.get_row(i)
        # Break out of loop if row is empty
        if not row:
            break
        # Append PledgeDict equivalent of row to variable 'pledges'
        pledges.append(gsparser.to_Pledge(row, header))

    # Update radiothonInfo to latest state
    radiothonInfo = gsparser.to_RadiothonInfo(pledges, config)

    # Log radiothonInfo update attempt success
    dbg.success("Server status update successful (poller.radiothonInfo updated)")

def update_config_status():
    '''
    Updates variable ‘config’ by loading server_config.json file as Dict
    :return: None
    '''

    global config

    # Attempt to load server config
    try:
        config = json.load(open('../server_config.json', 'r'))
    # Throw error if file does not exist
    except FileNotFoundError:
        dbg.err(
            "Could not read server config because server_config.json does not exist. server_config.json must be in project's root directory.")

def main(creds=0):
    '''
    Entrypoint for poller.py module

    :param server_config:
    :param creds:
    :return: None
    '''

    # Bring global variables into local scope
    global config
    global database

    # Initialize config for the first time
    update_config_status()

    # Instantiate new database instance linked to doc ID and worksheet ID specified in server_config.json
    database = Database(config["gsheets"]["doc_ID"], config["gsheets"]["wsheet_ID"], creds)

    # Update self periodically
    while True:
        update_radiothonInfo()
        sleep(config['gsheets']['poll_interval'] * 60)
