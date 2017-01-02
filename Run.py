from Socket import openSocket
from Initialize import joinRoom
from Read import getUser, getMessage

import string

s = openSocket()
joinRoom(s)
readBuffer = ""

while True:
	readBuffer = readBuffer + s.recv(1024)
	temp = string.split(readBuffer, "\n")
	readBuffer = temp.pop()
		
	for line in temp:
          print(line)
          user = getUser(line)
          message = getMessage(line)
          print(user + ": " + message)