#!/usr/bin/env python
#--*--coding:UTF-8 --*--

import socket,sys

buffer=4096

host = "127.0.0.1"
port = 6789

socket_server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socket_server.bind((host,port))

while True:
	data,addr = socket_server.recvfrom(buffer)
	data = data.strip()
	print "received from: ",addr
	print "message: ", data

	try:
		response = "Hi %s" % sys.platform
	except Exception,e:
		response = "%s" % sys.exc_info()[0]
	
	print "Response",response
	
	socket_server.sendto("%s "% response,addr)
		
socket_server.close()
		
