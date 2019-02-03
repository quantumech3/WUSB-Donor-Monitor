import threading

# Simulates a constantly running server process
def thread_1():
	while True:
		x = 0


# Start side thread
t1 = threading.Thread(target=thread_1, name="t1")

# Set side thread to be daemon so it stops when the rest of the program stops
t1.setDaemon(True)

# Start daemon thread
t1.start()

# Command line interface
while True:
	if input() == "exit":
		exit(0)
