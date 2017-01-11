# coding: utf-8
#==============================================================================
# Author       : Shaylyn Wetts
# Last Edited  : 01/05/17
#
# Run.py       : Opens the socket connection and joins the Twitch chat
#                specified in Configure.py.  Uses multithreading
#
# TODO: general functions list
#   - loyalty (revlo type functionality)
#   - song requests
#   - links to other streamers
#   - uptime
#   - request stream functionality (gotta determine how to go about this)
#       - store requests in a persistent file with username and message
#       - request stream mode must be active for requests to be taken
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
logFile = createChatLogFile()
bannedWords = readInBannedWords()
for word in bannedWords:
    print(word)
sock.send("CAP REQ :twitch.tv/commands\r\n") # allows bot to receive whispers

#==============================================================================
# main: reads in messages and commands from chat users and returns a PONG
#       when PINGed by Twitch; contains a specific set of requirements to
#       invoke the banUser() function
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
            messageType = getMessageType(readLine)
            print("( " + messageType + " ) " + username + ": " + message)
            chatLog(logFile, username, message, messageType)
            languageMod(sock, username, message, bannedWords)

            if message == "!links\r\n":
                printLinks(sock, logFile)
            elif message == "!commissions\r\n":
                printCommissionInfo(sock, logFile)
            elif message == "!requests\r\n":
                printRequestInfo(sock, logFile)
            elif message == "!software\r\n":
                printSoftware(sock, logFile)
            elif message == "!hardware\r\n":
                printHardware(sock, logFile)
            else:
                pass

            if messageType == "WHISPER":
                if username == "alfalfadil":
                    parts = message.split()
                    numParts = len(parts)
                    if numParts == 2:
                        if parts[0] == "!ban":
                            banMessage = "Banning user: " + parts[1] + "\r\n"
                            print(banMessage)
                            chatLog(logFile, "roreoBOT", banMessage, "CONSOLE OUTPUT")
                            banUser(sock, parts[1])
                        if parts[0] == "!timeout":
                            timeoutMessage = "Timing out user: " + parts[1] + "\r\n"
                            print(timeoutMessage)
                            chatLog(logFile, "roreoBOT", timeoutMessage, "CONSOLE OUTPUT")
                            timeoutUser(sock, parts[1])

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