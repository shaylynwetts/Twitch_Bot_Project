# coding: utf-8
#==============================================================================
# Author       : Shaylyn Wetts
# Last Edited  : 01/02/17
#
# Functions.py : Contain functions that can be called by user input to the
#                chat
#
# TODO:
#   * continue implementing languageMod function
#==============================================================================
from Setup import sendMessage

#==============================================================================
# printLinks (command !links): prints links to social media and professional
#                              pages
#==============================================================================
def printLinks(sock):
    twitterLink = "https://twitter.com/alfalfadil"
    tumblrLink = "https://alfalfadil.tumblr.com"
    message = "✖ LINKS ✖ twitter @ " + twitterLink + " ✖ tumblr @ " + tumblrLink
    sendMessage(sock, message)

#==============================================================================
# printCommissionInfo (command !commissions): prints link to main commission
#                                             info page on Tumblr
#==============================================================================
def printCommissionInfo(sock):
    commissionLink = "http://alfalfadil.tumblr.com/post/147679795591/commission-info"
    message = "✖ COMMISSIONS ✖ " + commissionLink
    sendMessage(sock, message)

#==============================================================================
# printRequestInfo (command !requests): prints link to requests info when that
#                                       is finished
#==============================================================================
def printRequestInfo(sock):
    requstsLink = "No Request Info Yet"
    message = "✖ REQUESTS ✖ " + requstsLink
    sendMessage(sock, message)

#==============================================================================
# printSoftware (command !software): prints information on software being
#                                    used for the stream
#==============================================================================
def printSoftware(sock):
    softwareInfo = "drawing program: Paint Tool SAI ✖ stream client: OBS"
    message = "✖ SOFTWARE ✖ " + softwareInfo
    sendMessage(sock, message)

#==============================================================================
# printHardware (command !hardware): prints information on hardware being
#                                    used for the stream
#==============================================================================
def printHardware(sock):
    hardwareInfo = "tablet: Wacom Cintiq 22HD"
    message = "✖ HARDWARE ✖ " + hardwareInfo
    sendMessage(sock, message)

#==============================================================================
# languageMod: searches a message sent from chat for banned words and issues
#              timeouts accordingly
#==============================================================================
#def languageMod(sock, user, originalMessage):
#    bannedWords = [
#
#    ]

#==============================================================================
# banUser: bans a user; bans can only be issued through whisper by specified
#          user
#==============================================================================
def banUser(sock, user):
    banMessage = ".ban "
    message = banMessage + user
    sendMessage(sock, message)

#==============================================================================
# timeoutUser: timeouts a user; done in response to the language mod
#==============================================================================
def timeoutUser(sock, user):
    timeoutMessage = ".timeout "
    message = timeoutMessage + user
    sendMessage(sock, message)