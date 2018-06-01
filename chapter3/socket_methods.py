# -*- encoding: utf-8 -*-

import socket
import sys

try:
   print "gethostbyname"
   print socket.gethostbyname_ex('www.google.com')
   print "\ngethostbyaddr"
   print socket.gethostbyaddr('8.8.8.8')
   print "\ngetfqdn"
   print socket.getfqdn('www.google.com')
   print "\ngetaddrinfo"
   print socket.getaddrinfo('www.google.com',socket.SOCK_STREAM)
   
except socket.error as error:
   print (str(error))
   print ("Connection error")
   sys.exit()
   
