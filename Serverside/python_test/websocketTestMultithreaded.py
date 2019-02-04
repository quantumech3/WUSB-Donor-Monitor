import asyncio
import websockets
import threading



def webThread():
    # Gets called when someone logins to websocket server
    async def handleLogin(websocket, path):
        print("A new friend logged in :D")

        # Send the text 'a message' to client
        await websocket.send("A message")

    # Create an event loop just for this thread.
    # You must do this BEFORE you instantiate a socket server otherwise...
    # ...you will get a runtime error
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # Instantiate Websocket server
    start_server = websockets.serve(handleLogin, "localhost", 8080)

    # Launch server as async process
    loop.run_until_complete(start_server)

    # Run forever after login is handled
    loop.run_forever()


socket = threading.Thread(target=webThread, name="t1")
socket.start()

# Something that happens on main thread
print("pi")