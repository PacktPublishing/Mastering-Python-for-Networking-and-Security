#!/usr/bin/env python
#--*-- coding:UTF-8 --*--

import socket,sys

host = "domain/ip_address"
port = 9999


try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error,e:
	print "socket create error: %s" %e
	sys.exit(1)

try:
	s.connect((host,port))
except socket.timeout,e :
	print "Timeout %s" %e
	sys.exit(1)
except socket.gaierror, e:
	print "connection error to the server:%s" %e
	sys.exit(1)
except socket.error, e:
	print "Connection error: %s" %e
	sys.exit(1)



