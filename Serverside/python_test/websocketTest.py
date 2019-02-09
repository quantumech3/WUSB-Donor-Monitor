import asyncio
import websockets


# Event that gets called when someone logs in to Websockets server
async def handleLogin(websocket, path):
    print("A new friend logged in :D")

    # Send the text 'a message' to client
    await websocket.send("A message")

# Instantiate Websocket server with 'handleLogin()' handling events and hosting from address 'localhost' on port 8080
start_server = websockets.serve(handleLogin, "0.0.0.0", 8000)

# Launch server as async process (Must be an async process according to the api)
asyncio.get_event_loop().run_until_complete(start_server)

# Run forever after login is handled (Infinite event loop must occur because Websockets constantly polls for events)
asyncio.get_event_loop().run_forever()