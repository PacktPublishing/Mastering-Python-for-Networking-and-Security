#!/usr/bin/env python
# --*-- coding: UTF-8 --*--
import sys, socket
result=socket.getaddrinfo("www.google.es",None,0,socket.SOCK_STREAM)
print result
print result[0][4]
for item in result:
	print "%s" % (str(item[4]))

