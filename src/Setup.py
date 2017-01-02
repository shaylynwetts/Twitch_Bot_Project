from Configure import *

import socket
import string

def openSocket():
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send("PASS " + PASS + "\r\n")
    s.send("NICK " + NICK + "\r\n")
    s.send("JOIN #" + CHANNEL + "\r\n")
    return s

def sendMessage(s, message):
    messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
    s.send(messageTemp + "\r\n")
    print("Sent: " + messageTemp)

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

def getUser(line):
    separate = line.split(":", 2)
    user = separate[1].split("!", 1)[0]
    return user

def getMessage(line):
    separate = line.split(":", 2)
    message = separate[2]
    return message
