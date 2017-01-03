# coding: utf-8
#==============================================================================
# Author       : Shaylyn Wetts
# Last Edited  : 01/02/17
#
# Run.py       : Opens the socket connection and joins the Twitch chat
#                specified in Configure.py.  Uses multithreading
#
# TODO: general functions list
#   - parse for language for timing out
#   - basic input output commands & cycle them output
#       * commission info & availability
#       * drawing programs
#       * tablet
#       * requests info
#   - chat log
#   - loyalty (revlo type functionality)
#   - song requests
#   - links to other streamers
#   - uptime
#   - request stream functionality (gotta determine how to go about this)
#
#==============================================================================
from Setup import *
from Functions import *
from Configure import RATE

import string
import time
import threading

sock = openSocket()
joinRoom(sock)

#==============================================================================
# main: reads in messages and commands from chat users and returns a PONG
#       when PINGed by Twitch
#==============================================================================
def main():
    while True:
        readLine = sock.recv(1024).decode("utf-8")

        if readLine == "PING :tmi.twitch.tv\r\n":
            print("PINGed")
            sock.send("PONG :tmi.twitch.tv\r\n")
            print("PONGed\n")
        else:
            username = getUsername(readLine)
            message = getMessage(readLine)
            print(username + ": " + message)

            if message == "!links\r\n":
                printLinks(sock)

        time.sleep(1 / RATE)

#==============================================================================
# outputCycle: cycles through various output commands (minutes * seconds)
#==============================================================================
def outputCycle():
    while True:
        time.sleep(2 * 60)
        printLinks(sock)


#==============================================================================
# runs multiple threads so reading in from the chat does not affect cycling
# output and vice versa
#==============================================================================
threadMain = threading.Thread(target=main)
threadMain.daemon = True
threadMain.start()

threadOutputCycle = threading.Thread(target=outputCycle)
threadOutputCycle.daemon = True
threadOutputCycle.start()

while True:
    persist = 1