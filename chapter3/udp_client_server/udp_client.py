#!/usr/bin/env python
#--*--coding:UTF-8 --*--

import socket

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT = 6789

buffer=4096

address = (UDP_IP_ADDRESS ,UDP_PORT)

socket_client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
	message = raw_input('?: ').strip()
	if message=="quit":
		break
	socket_client.sendto("%s" % message,address)
	response,addr = socket_client.recvfrom(buffer)
	print "=> %s" % response
		
socket_client.close()
		
