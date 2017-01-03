#==============================================================================
# Author       : Shaylyn Wetts
# Last Edited  : 01/02/17
#
# Setup.py     : Contains functions for connecting to Twitch as well as the
#                basic functions for sending and interpreting messages read
#                by the bot
#==============================================================================

from Configure import *

import socket
import string

#==============================================================================
# openSocket: opens a socket connection between the bot and Twitch chat using
#             the auth code, bot username, and channel username
#==============================================================================
def openSocket():
    sock = socket.socket()
    sock.connect((HOST, PORT))
    sock.send("PASS " + PASS + "\r\n")
    sock.send("NICK " + NICK + "\r\n")
    sock.send("JOIN #" + CHANNEL + "\r\n")
    return sock

#==============================================================================
# sendMessage: sends a message from the bot to the connected Twitch chat
#              as well as outputs the message to the terminal
#==============================================================================
def sendMessage(sock, message):
    messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
    sock.send(messageTemp + "\r\n")
    print("ROREOBOT sent: " + messageTemp)

#==============================================================================
# joinRoom: bot reads in all info from Twitch chat as it connects and sends
#           a message to the chat once finished
#==============================================================================
def joinRoom(sock):
    readBuffer = ""
    loading = True
    while loading:
        readLine = sock.recv(1024).decode("utf-8")

        print(readLine)
        loading = loadingComplete(readLine)
        
    sendMessage(sock, "CoolCat CoolCat")

#==============================================================================
# loadingComplete: determines the end of info read in from Twitch chat
#                  as the bot connects
#==============================================================================
def loadingComplete(readLine):
    if("End of /NAMES list" in readLine):
        return False
    else:
        return True

#==============================================================================
# getUsername: splits the username of a chat user from the rest of the
#              information read in by the bot
#==============================================================================
def getUsername(readLine):
    parts = readLine.split(":", 2)
    username = parts[1].split("!", 1)[0]
    return username

#==============================================================================
# getMessage: splits the message of a chat user from the rest of the
#             information read in by the bot
#==============================================================================
def getMessage(readLine):
    parts = readLine.split(":", 2)
    message = parts[2]
    return message
