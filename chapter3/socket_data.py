#!/usr/bin/python
#-*- coding: utf-8 -*-

import socket

print 'creating socket ...'
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print 'socket created'
print "connection with remote host"
s.connect(('www.google.com',80))
print 'connection ok'
s.send( 'GET /index.html HTML/1.1\r\n\r\n')
while 1:
	data=s.recv(128)
	print data
	if data== "":
		break
print 'closing the socket'
s.close()
