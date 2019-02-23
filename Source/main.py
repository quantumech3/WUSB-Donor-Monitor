# -*- coding: utf-8 -*-
'''
Created by Scott Burgert on 2/17/2019
Project name: WUSB Donor Monitor ©

Module name: main.py
Module description:
        This module is what gets started when ‘start_server.sh’ is ran.
    This module starts the ‘poller.py’ module, ‘host.py’ module and the ‘cmd.py’ module.
'''

import pickle
import json
import poller
import threading
from time import sleep
import host

creds = pickle.load(open('./creds.pickle', 'rb'))

config = {}

with open("../server_config.json", 'r') as file:
    config = json.load(file)

t1 = threading.Thread(target=poller.main, args=[creds])
t2 = threading.Thread(target=host.main)

t1.start()
t2.start()