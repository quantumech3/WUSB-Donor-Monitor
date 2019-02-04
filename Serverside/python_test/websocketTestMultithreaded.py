import asyncio
import websockets
import threading
import http.server
import socketserver
import json

def webSocket():
    # Gets called when someone logins to websocket server
    async def handleLogin(websocket, path):
        print("A new friend logged in :D")

        # Send credentials json to client
        await websocket.send(open("credentials.json").read())

        # Print message sent back from client
        print(await websocket.recv())

    # Create an event loop just for this thread.
    # You must do this BEFORE you instantiate a socket server otherwise...
    # ...you will get a runtime error
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # Instantiate Websocket server
    start_server = websockets.serve(handleLogin, "localhost", 8000)

    # Launch server as async process
    loop.run_until_complete(start_server)

    # Run loop continuously to allow checking for login
    loop.run_forever()


def httpServer():
    reqHandler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", 8080), reqHandler) as server:
        server.serve_forever()


socketThread = threading.Thread(target=webSocket)
httpThread = threading.Thread(target=httpServer)
socketThread.start()
httpThread.start()

# Something that happens on main thread
print("pi")