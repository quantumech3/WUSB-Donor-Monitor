from flask import Flask, send_file, send_from_directory
from flask_socketio import SocketIO

# Instantiate Flask server with the name of this module as its 'import_name'
app = Flask(__name__)

# Instantiate SocketIO server and bind it to flask app
socketio = SocketIO(app)

# When client requests root, send client index.html
@app.route("/")
def home():
    # Sends data inside index.html back to client
    return send_file("websocketTest.html")

# 'path', inside of @app.route(), is a variable whose type is ironically named 'path' (like string but allows slashes)
# Variables specified inside of app.route get mapped to parameters in function
# Variables in route() are defined by <type: name>
@app.route("/<path:path>")
def res(path):
    # Sends string back to client from whatever path the client requested inside ./webpage/*
    # YOU SHOULD NOT PUT A SLASH BEFORE THE FIRST ARGUEMENT IN send_file BECAUSE IT WILL NOT LOAD THE FILE BECAUSE
    # IT WOULD TRY TO LOAD FROM './/webpage/*' which doesnt make any sence
    try:
        return send_file("webpage/"+path)
    except FileNotFoundError:
        print("Could not retrieve file for client: " + path)
        return "<b>Could not retrieve file from server... Sorry :(</b>"

# Event that runs on SocketIO 'message' event sent from client
@socketio.on("message")
def msg_event(msg):
    print(msg['data'])


if __name__ == "__main__":
    # Run SocketIO server on top of 'app' HTTP server
    socketio.run(app, host="0.0.0.0", port=8000)
