import asyncio

# Meant to simulate the Google Sheets API and the
async def asyncFunc():
	while True:
		print("Xd")
		# Tells thread to complete after a second
		print("Xd") # Therefore this statement will never execute

async def console():
	while True:
		cmd = input()

		if cmd == "exit":
			asyncio.get_event_loop().stop()
			return

async def mainAsync():
	# First thread being scheduled
	asyncio.ensure_future(asyncFunc())
	# Second thread being scheduled
	asyncio.ensure_future(console())

# Get event stack
loop = asyncio.get_event_loop()

# Append main scheduling thread to event stack and run it
loop.run_until_complete(mainAsync())
