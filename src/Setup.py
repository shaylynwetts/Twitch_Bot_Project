# coding: utf-8
#==============================================================================
# Author       : Shaylyn Wetts
# Last Edited  : 01/05/17
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
#             information read in by the bot.  Handles receive messages that
#             do not contain a message part
#==============================================================================
def getMessage(readLine):
    parts = readLine.split(":", 2)
    numParts = len(parts)
    if numParts != 3:
        message = " "
    else:
        message = parts[2]
    return message

#==============================================================================
# getMessageType: determines whether a message is a regular message from
#                 a user in chat (PRIVMSG) or a whisper (WHISPER)
#==============================================================================
def getMessageType(readLine):
    parts = readLine.split()
    messageType = ""
    if "WHISPER" in parts:
        messageType = "WHISPER"
    if "PRIVMSG" in parts:
        messageType = "PRIVMSG"
    return messageType
