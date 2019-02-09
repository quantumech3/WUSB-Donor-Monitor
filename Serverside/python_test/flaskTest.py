from flask import Flask, send_file, send_from_directory

app = Flask(__name__)

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
    return send_file("webpage/"+path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)