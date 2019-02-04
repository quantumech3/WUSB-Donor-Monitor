import asyncio
import websockets


# Gets called when someone logins to websocket server
async def handleLogin(websocket, path):
    print("A new friend logged in :D")

    # Send the text 'a message' to client
    await websocket.send("A message")

# Instantiate Websocket server
start_server = websockets.serve(handleLogin, "localhost", 8080)

# Launch server as async process
asyncio.get_event_loop().run_until_complete(start_server)

# Run forever after login is handled
asyncio.get_event_loop().run_forever()
print("pi")