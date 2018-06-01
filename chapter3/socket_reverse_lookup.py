#!/usr/bin/env python
# --*-- coding: UTF-8 --*--

import sys, socket
try :
	result=socket.gethostbyaddr("8.8.8.8")
	print "The host name is:"
	print " "+result[0]
	print "\nAddress:"
	for item in result[2]:
		print " "+item
except socket.herror,e:
	print "error for resolving ip address:",e

