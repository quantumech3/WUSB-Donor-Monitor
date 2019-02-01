import asyncio

# Meant to simulate the Google Sheets API and the
async def asyncFunc():
	while(True):
		print("Xd")
		# Tells thread to complete after a second
		await asyncio.sleep(1)
		print("Xd") # Therefore this statement will never execute

async def console():
	while True:
		cmd = input()

		if cmd == "exit":
			exit(0)

async def mainAsync():
	# First thread being scheduled
	asyncio.ensure_future(asyncFunc())
	# Second thread being scheduled
	asyncio.ensure_future(console())
	# TODO: Figure out how to make a 'Task exception' handler
	# TODO: Once you figure that out, then write down how this will apply to WebSocket vs the console

# Get event stack
loop = asyncio.get_event_loop()

# Append main scheduling thread to event stack and run it
loop.run_until_complete(mainAsync())
