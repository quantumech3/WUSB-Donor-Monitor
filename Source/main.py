# -*- coding: utf-8 -*-
'''
Created by Scott Burgert on 2/17/2019
Project name: WUSB Donor Monitor ©

Module name: main.py
Module description:
        This module is what gets started when ‘start_server.sh’ is ran.
    This module starts the ‘poller.py’ module, ‘host.py’ module and the ‘cmd.py’ module.
'''


from flask import Flask, send_from_directory
from flask_socketio import SocketIO

app = Flask(__name__)
socket = SocketIO(app)


@app.route("/")
def homepage():
    return send_from_directory('Website', 'index.html')

@app.route("/<path:path>")
def other(path):
    return send_from_directory("Website", path)

@socket.on("connect")
def new_connection():
    socket.emit('pageData', {
        'name': 'WUSB R 2019',
        'startDate': '2/19/19',
        'endDate': '2/20/19',
        'goalHourly': 2000,
        'goalDaily': 4000,
        'goalWeekly': 8000,
        'goalTotal': 16000,
        'pledges': [{
            'firstName': 'Bobby',
            'city': 'Port Jefferson',
            'amtDonated': 4297,
            'pledgeType': 0,
            'paidByCredit': True,
            'isPaid': True
        }]
    })

socket.run(app, host='0.0.0.0', port=8080)