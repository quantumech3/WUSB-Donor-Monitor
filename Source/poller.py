# -*- coding: utf-8 -*-
'''
Created by Scott Burgert on 2/20/2019
Project name: WUSB Donor Monitor ©

Module name: poller.py
Module description:
        This module runs on an independent daemon thread and has an entry point that is called by the ‘main.py’ module.
        This module’s purpose is to poll for GSheets pledge information on a certain interval asynchronously.
        The data processed from this module can be accessed by other module by either referencing the 'radiothonInfo'
        or the 'config' variables.
'''

import gsparser
from database import Database
from time import sleep
import threading
import debug as dbg
import json
import os

# This var is set by the cmd.py module when ‘reload’ command is called and on startup and is a server_config Dict
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

    # Attempt to refresh GAPI credentials. Needed otherwise Google will reject requests after certain period of time.
    dbg.log("Attempting to refresh GAPI credentials")
    database.gs.login()
    dbg.success("Successfully refreshed GAPI credentials")

    # Update config
    update_config_status()

    # Log radiothonInfo update attempt
    dbg.log("Attempting to update server status (poller.radiothonInfo)")

    # Get all rows from Google sheets document
    dbg.log("Attempting to get all the data from GSheets document.")
    rows = database.get_all_vals()
    dbg.success("Successfully got all data from GSheets document.")

    # Throw error and exit if there is no data in GSheets document at all
    if len(rows) == 0:
        dbg.err("Failed to update server status because there is no data or header in Google Sheets document")
        input("Cannot continue. Press any key to exit.")
        os._exit(-1)

    # Get header from GSheets doc to compare pledges against.
    header = rows[0]

    # PledgeDict accumulator. Will contain a list of 'Pledge' data structures
    pledges = []

    # Get all rows with content excluding header (which is why i starts at 1)
    # from GSheets doc and turn them into PledgeDict's
    for i in range(1, len(rows)):
        pledges.append(gsparser.to_Pledge(rows[i], header))

    # Update radiothonInfo to latest state
    radiothonInfo = gsparser.to_RadiothonInfo(pledges, config)

    # Log that radiothonInfo was successfully updated
    dbg.success("Server status update successful (poller.radiothonInfo updated)")


def update_config_status():
    '''
    Updates variable ‘config’ by loading server_config.json file as Dict
    :return: None
    '''

    def handle_corrupt_key(dict={}, key_name="", types_allowed=None):
        '''
        Throws error and quits if a key with name set to value of 'key_name' does not exist or if the value associated
        with the key is not set to type 'types_allowed'
        Used primarily to test for corrupted server_config.json.

        :param dict: ServerConfigDict
        :param key_name: Str
        :param types_allowed: Type[]
        :return: None
        '''

        # Attempt to get value from key
        try:
            # Throw error and exit if value associated with key is not of any types specified in 'types_allowed'
            if type(dict[key_name]) not in types_allowed:
                # Print error message "Failed to read server_config.json. The '<key_name>' key must be set to one of the following data types: ['typename',...]"
                dbg.err(
                    "Failed to read server_config.json. The '" + key_name + "' key needs must be set to one of the following data types: " +
                    str([i.__name__ for i in types_allowed]))

                # Prompt for input then exit
                input("Cannot continue. Press any key to exit..")
                os._exit(-1)

        # Throw error and exit if key cannot be found
        except KeyError:
            dbg.err("Failed to read server_config.json. '" + key_name + "' key does not exist in server_config.json.")
            input("Cannot continue. Press any key to exit..")
            os._exit(-1)

    global config

    # Attempt to load server config and throw error if any keys either don't exist or have an invalid type
    try:
        # Log attempt
        dbg.log("Attempting to update server config status")

        # Attempt to load JSON from server_config.json as type Dict
        config = json.load(open('../server_config.json', 'r'))

        # Throw error if any keys in server_config.json are either missing or invalidly typed
        handle_corrupt_key(config, "radiothon", [dict])
        handle_corrupt_key(config["radiothon"], "goal", [dict])
        handle_corrupt_key(config["radiothon"], "name", [str])
        handle_corrupt_key(config["radiothon"], "start_date", [str])
        handle_corrupt_key(config["radiothon"], "end_date", [str])
        handle_corrupt_key(config["radiothon"]["goal"], "hourly", [float, int])
        handle_corrupt_key(config["radiothon"]["goal"], "daily", [float, int])
        handle_corrupt_key(config["radiothon"]["goal"], "weekly", [float, int])
        handle_corrupt_key(config["radiothon"]["goal"], "total", [float, int])
        handle_corrupt_key(config, "gsheets", [dict])
        handle_corrupt_key(config["gsheets"], "doc_ID", [str])
        handle_corrupt_key(config["gsheets"], "wsheet_ID", [int])
        handle_corrupt_key(config["gsheets"], "poll_interval", [float, int])

    # Throw error if file does not exist
    except FileNotFoundError:
        dbg.err(
            "Failed to read server config because server_config.json does not exist. server_config.json must be in project's root directory.")
        input("Cannot continue. Press any key to exit")
        os._exit(-1)

    # Throw error if JSON from server_config.json could not be parsed
    except json.JSONDecodeError as e:
        dbg.err("Failed to read server_config.json. JSON Decoder threw the following error: \n'" + str(e) + "'")
        input("Cannot continue. Press any key to exit.")
        os._exit(-1)

    # Log config loading success
    dbg.success("Server config status successfully updated")


def main(creds=0):
    '''
    Entry point for poller.py module

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
