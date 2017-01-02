from Configure import *

import socket
import string

def openSocket():
    sock = socket.socket()
    sock.connect((HOST, PORT))
    sock.send("PASS " + PASS + "\r\n")
    sock.send("NICK " + NICK + "\r\n")
    sock.send("JOIN #" + CHANNEL + "\r\n")
    return sock

def sendMessage(sock, message):
    messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
    sock.send(messageTemp + "\r\n")
    print("Sent: " + messageTemp)

def joinRoom(sock):
    readBuffer = ""
    loading = True
    while loading:
        readLine = sock.recv(1024).decode("utf-8")

        print(readLine)
        loading = loadingComplete(readLine)
        
    sendMessage(sock, "Succesfully joined chat")

def loadingComplete(readLine):
    if("End of /NAMES list" in readLine):
        return False
    else:
        return True

def getUsername(readLine):
    parts = readLine.split(":", 2)
    username = parts[1].split("!", 1)[0]
    return username

def getMessage(readLine):
    parts = readLine.split(":", 2)
    message = parts[2]
    return message
