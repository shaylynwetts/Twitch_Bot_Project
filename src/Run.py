#==============================================================================
# TODO: make a new file for general functions
#
# TODO: general functions list
#	- parse for language for timing out
#	- basic input output commands & cycle them output
#		* links
#		* commission info & availability
#		* drawing program
#		* tablet
#	- chat log
#	- loyalty (revlo type functionality)
#	- song requests
#	- links to other streamers
#	- uptime
#
# TODO: comments
#==============================================================================
from Setup import *
from Configure import RATE

import string
import time

s = openSocket()
joinRoom(s)

while True:
	line = s.recv(1024).decode("utf-8")

	if line == "PING :tmi.twitch.tv\r\n":
		print("PINGed")
		s.send("PONG :tmi.twitch.tv\r\n")
		print("PONGed\n")
	else:
		user = getUser(line)
		message = getMessage(line)
		print(user + ": " + message)

	time.sleep(1 / RATE)
#==============================================================================
#   Sample of responding to a specific string in a message
#           if "string" in message:
#               sendMessage(s, "response")
#==============================================================================