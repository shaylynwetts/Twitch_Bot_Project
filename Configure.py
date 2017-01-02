passFile = open('oauthToken.txt', 'r')

HOST = "irc.twitch.tv"
PORT = 6667
PASS = passFile.read()
NICK = "roreobot"
CHANNEL = "alfalfadil"
