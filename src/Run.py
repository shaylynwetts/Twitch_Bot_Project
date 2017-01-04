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
#   - chat log
#   - loyalty (revlo type functionality)
#   - song requests
#   - links to other streamers
#   - uptime
#   - request stream functionality (gotta determine how to go about this)
#       - store requests in a persistent file with username and message
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
            elif message == "!commissions\r\n":
                printCommissionInfo(sock)
            elif message == "!requests\r\n":
                printRequestInfo(sock)
            elif message == "!software\r\n":
                printSoftware(sock)
            elif message == "!hardware\r\n":
                printHardware(sock)
            else:
                pass

        time.sleep(1 / RATE)

#==============================================================================
# outputCycle: cycles through various output commands (minutes * seconds)
#==============================================================================
def outputCycle():
    while True:
        time.sleep(5 * 60)
        printLinks(sock)
        time.sleep(5 * 60)
        printCommissionInfo(sock)
        time.sleep(5 * 60)
        printRequestInfo(sock)
        time.sleep(5 * 60)
        printSoftware(sock)
        time.sleep(5 * 60)
        printHardware(sock)

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