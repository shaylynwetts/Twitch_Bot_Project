# coding: utf-8
#==============================================================================
# Author       : Shaylyn Wetts
# Last Edited  : 01/02/17
#
# Functions.py : Contain functions that can be called by user input to the
#                chat
#
# TODO:
# def printLinks():
#
# def printCommissionInfo():
#
# def printRequestInfo():
#
# def printSoftware():
#
# def printHardware():
#==============================================================================
from Setup import sendMessage


#==============================================================================
# printLinks (command !links): prints links to social media and professional
#                              pages
#==============================================================================
def printLinks(sock):
    twitterLink = "https://twitter.com/alfalfadil"
    tumblrLink = "https://alfalfadil.tumblr.com"
    message = "✖ LINKS ✖ Twitter @ " + twitterLink + " ✖ Tumblr @ " + tumblrLink
    sendMessage(sock, message)
