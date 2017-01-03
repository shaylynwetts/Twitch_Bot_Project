# coding: utf-8
#==============================================================================
# Author       : Shaylyn Wetts
# Last Edited  : 01/02/17
#
# Functions.py : Contain functions that can be called by user input to the
#                chat
#
# TODO:
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