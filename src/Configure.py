#==============================================================================
# Author       : Shaylyn Wetts
# Last Edited  : 01/02/17
#
# Configure.py : Contains basic information for connecting to Twitch
#                
#==============================================================================

passFile = open('oauthToken.txt', 'r') # contains authentication token for bot
                                       # account
HOST = "irc.twitch.tv"                 # host ID
PORT = 6667                            # port
PASS = passFile.read()                 # auth token
NICK = "roreobot"                      # bot username
CHANNEL = "alfalfadil"                 # channel username
RATE = (0.667)                         # message rate
