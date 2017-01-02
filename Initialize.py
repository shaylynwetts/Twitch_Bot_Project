from Socket import sendMessage
import string

def joinRoom(s):
	readBuffer = ""
	loading = True
	while loading:
		readBuffer = readBuffer + s.recv(1024)
		temp = string.split(readBuffer, "\n")
		readBuffer = temp.pop()
		
		for line in temp:
			print(line)
			loading = loadingComplete(line)
	sendMessage(s, "Succesfully joined chat")

def loadingComplete(line):
	if("End of /NAMES list" in line):
		return False
	else:
		return True
