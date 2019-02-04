import http.server
import socketserver
import socket

# Port server is running on
PORT = 8080

# Instantiate the http handler (i.e the thing that has the instructions for how to handle http events)
handler = http.server.SimpleHTTPRequestHandler

# Initializes server object using localhost (the blank string defaults to localhost) using the port specified by 'PORT'
with socketserver.TCPServer(("", PORT), handler) as httpServer:
    # Launch server
    httpServer.serve_forever()
    httpServer.socket.send("Content-type: image/jpeg")