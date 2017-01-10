# coding: utf-8
#==============================================================================
# Author       : Shaylyn Wetts
# Last Edited  : 01/05/17
#
# Functions.py : Contain functions that can be called by user input to the
#                chat
#
# TODO:
#
#==============================================================================
from Setup import sendMessage

#==============================================================================
# printLinks (command !links): prints links to social media and professional
#                              pages
#==============================================================================
def printLinks(sock, currentLog):
    twitterLink = "https://twitter.com/alfalfadil"
    tumblrLink = "https://alfalfadil.tumblr.com"
    message = "✖ LINKS ✖ twitter @ " + twitterLink + " ✖ tumblr @ " + tumblrLink + "\r\n"
    sendMessage(sock, message)
    chatLog(currentLog, "roreoBOT", message, "PRIVMSG")

#==============================================================================
# printCommissionInfo (command !commissions): prints link to main commission
#                                             info page on Tumblr
#==============================================================================
def printCommissionInfo(sock, currentLog):
    commissionLink = "http://alfalfadil.tumblr.com/post/147679795591/commission-info"
    message = "✖ COMMISSIONS ✖ " + commissionLink + "\r\n"
    sendMessage(sock, message)
    chatLog(currentLog, "roreoBOT", message, "PRIVMSG")

#==============================================================================
# printRequestInfo (command !requests): prints link to requests info when that
#                                       is finished
#==============================================================================
def printRequestInfo(sock, currentLog):
    requstsLink = "No Request Info Yet"
    message = "✖ REQUESTS ✖ " + requstsLink + "\r\n"
    sendMessage(sock, message)
    chatLog(currentLog, "roreoBOT", message, "PRIVMSG")

#==============================================================================
# printSoftware (command !software): prints information on software being
#                                    used for the stream
#==============================================================================
def printSoftware(sock, currentLog):
    softwareInfo = "drawing program: Paint Tool SAI ✖ stream client: OBS"
    message = "✖ SOFTWARE ✖ " + softwareInfo + "\r\n"
    sendMessage(sock, message)
    chatLog(currentLog, "roreoBOT", message, "PRIVMSG")

#==============================================================================
# printHardware (command !hardware): prints information on hardware being
#                                    used for the stream
#==============================================================================
def printHardware(sock, currentLog):
    hardwareInfo = "tablet: Wacom Cintiq 22HD"
    message = "✖ HARDWARE ✖ " + hardwareInfo + "\r\n"
    sendMessage(sock, message)
    chatLog(currentLog, "roreoBOT", message, "PRIVMSG")

#==============================================================================
# languageMod: searches a message sent from chat for banned words and issues
#              timeouts accordingly
#==============================================================================
def languageMod(sock, user, originalMessage):
    bannedWords = [
        "cuckold"
    ]

    for word in bannedWords:
        if word in originalMessage:
            print(user + " has been timed out due to language.")
            timeoutUser(sock, user)

#==============================================================================
# banUser (!ban username): bans a user; bans can only be issued through
#                          whisper by specified user
#==============================================================================
def banUser(sock, user):
    banMessage = ".ban "
    message = banMessage + user
    sendMessage(sock, message)

#==============================================================================
# timeoutUser (!timeout username): timeouts a user; done in response to the
#                                  language mod or through whisper by specified
#                                  user
#==============================================================================
def timeoutUser(sock, user):
    timeoutMessage = ".timeout "
    message = timeoutMessage + user
    sendMessage(sock, message)

#==============================================================================
# chatLog: keeps a running log of all chat messages, including those
#          sent by roreoBOT.  File is stored in the logs directory
#==============================================================================
def chatLog(currentLog, username, message, messageType):
    currentLog = open(currentLog, "a")
    currentLog.write("( " + messageType + " ) " + username + ": " + message)
