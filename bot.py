#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import socket
from time import gmtime, strftime
from subprocess import call
import sys
import os
from pprint import pprint

def say(to, what):
        irc.send ( 'PRIVMSG %s :%s\r\n' % (to, what))

network = 'uevora.ptnet.org'
port = 6667
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
irc.connect ( ( network, port ) )
botnick = 'py'
canal = '#4chan'

irc.send ( 'NICK %s\r\n' % botnick)
irc.send ( 'USER %s %s %s :%s\r\n' % (botnick, botnick, botnick, botnick) )
flag=False

while True:
	data = irc.recv ( 4096 )
	print data
	if data.find ( 'PING :' ) != -1:
		newdata=data.split('PING :')[1]
		irc.send( 'PONG :' + newdata.split()[0] + '\r\n' )
		flag=True
	if flag:
		irc.send ( 'JOIN %s\r\n' % canal)
		flag=False
	if data.lower().find ( 'portugal' ) != -1:
		say(canal, "Portugal, LOL")
