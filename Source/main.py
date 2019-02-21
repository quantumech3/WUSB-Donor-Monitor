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
from database import Database
import gsparser

creds = pickle.load(open('creds.pickle', 'rb'))

database = Database("14xbkoqICLY-rcWnAOSJrLQkprKUJueQvZ4vkWfan-fI", 0, creds)

for i in range(6):
    print(gsparser.to_Donor(database.get_row(1 + i), database.get_row(0)))