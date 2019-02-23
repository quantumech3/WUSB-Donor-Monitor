# -*- coding: utf-8 -*-
'''
Created by Scott Burgert on 2/21/2019
Project name: WUSB Donor Monitor ©

Module name: host.py
Module description:
        This module runs on an independent daemon thread. This module has an entry point that is called by the ‘main.py’ module.
    This modules purpose is to host HTTP server and send data to client via SocketIO.
    All methods are declared inside the entry point because that is where they have to be declared in order for Flask to
    recognize them as events.
'''

import logging
import eventlet
from flask import Flask, send_from_directory
from flask_socketio import SocketIO
import debug as dbg
import poller
from time import sleep
import threading

# TODO: Make main.py silence external logging instead of host.py
if not dbg.VERBOSE:
    # Mute all logging from all external modules (mutes all logging up to level 'fatal' for everything)
    logging.basicConfig(level=logging.FATAL)

# Instantiate Flask HTTP server
http = Flask(__name__)

# Instantiate SocketIO server with 'threading' mode enabled.
socket = SocketIO(http, async_mode='threading')

def emit_pageData():
    '''
    Emits 'pageData' event and sends 'poller.radiothonInfo' RadiothonInfo data structure to client
    :return: None
    '''

    # Log 'pageData' event emitting attempt
    dbg.log("Attempting to emit 'pageData' event")

    # If radiothonInfo is done being processed, send 'pageData' event containing radiothonInfo to client
    if poller.radiothonInfo:
        socket.emit('pageData', poller.radiothonInfo)
        dbg.success("'pageData' event successfully emitted")
    # Else throw a warning
    else:
        dbg.warn("Was not able to emit 'pageData' SocketIO event. Didn't have enough time to process 'poller.radiothonInfo'")


def main():
    '''
    Main entry point for host.py module
    :return: void
    '''

    # Bring global variables into local scope
    global http
    global socket

    # These constant variables specify port and address for server to run on
    # '0.0.0.0' tells OS to make server visible to other computers on network
    ADDRESS = '0.0.0.0'
    PORT = 80

    # Thread that the server runs on (daemon thread)
    server_thread = threading.Thread(target=socket.run, args=[http, ADDRESS, PORT])
    server_thread.setDaemon(True)

    # Sends html from ‘./Website/index.html’
    @http.route('/')
    def http_homepage():
        '''
        Sends html from ‘./Website/index.html' when client connects
        '''

        # Attempt to send homepage to client
        dbg.log("Attempting to send './Website/index.html' to clients")

        # Test if ./Website/index.html exists. Throw error and exit if it doesn't
        try:
            open('./Website/index.html', 'r')
        except FileNotFoundError:
            dbg.err("Failed to send homepage to client because './Website/index.html' does not exist.")
            input("Server cannot run without homepage... Press any key to exit.")
            exit(-1)

        # Send html to client
        html = send_from_directory('./Website/', 'index.html')
        dbg.success("'./Website/index.html' successfully retrieved. Sending to clients...")
        return html

    # Sends html from ‘./Website/{path}’
    @http.route('/<path:path>')
    def http_other(path):
        '''
        Sends html from ‘./Website/{path} when client connects
        '''

        # Attempt to send homepage to client
        dbg.log("Attempting to send './Website/" + path + "' to clients")

        # Test if ./Website/<path> exists. Throw error if it doesn't.
        # Wont exit because something like 'favicon.ico' might not be integral to the application
        try:
            open('./Website/' + path, 'r')
        except FileNotFoundError:
            dbg.err("Failed to send file './Website/" + path + "' to clients . File does not exist.")

        # Send html to client
        html = send_from_directory('./Website/', path)
        dbg.success("'./Website/" + path + "' successfully retrieved. Sending to client...")
        return html

    # Emit pageData event when clients connect
    @socket.on('connect')
    def socket_connect():
        '''
        Emit a ‘pageData’ event and send poller.radiothonInfo to clients when a client connects
        '''

        emit_pageData()

    # Attempt to start server on port 80
    try:
        # Start server
        dbg.log("Attempting to start SocketIO/HTTP server on address '" + ADDRESS + ":" + str(PORT) + "'...")
        server_thread.start()

        # Log success
        dbg.success("Successfully started server")
    # If server fails to start, throw error
    except Exception as e:
        dbg.err("Failed to start SocketIO/HTTP server on address '" + ADDRESS + ":" + str(PORT) + "'. Flask threw the following error: \n" + str(e))
        print("Cannot continue. Press any key to exit.")
        exit(-1)

    # Periodically send 'pageData' event to client at interval specified in config
    while True:
        # Send pageData event and 'radiothonInfo' data structure to client
        emit_pageData()

        # If poller.config exists
        if poller.config['gsheets'] is not None:
            # Sleep for however long was specified in config
            sleep(poller.config['gsheets']['poll_interval'] * 60)
        # Else sleep for a second and try to emit pageData event again
        else:
            sleep(1)
