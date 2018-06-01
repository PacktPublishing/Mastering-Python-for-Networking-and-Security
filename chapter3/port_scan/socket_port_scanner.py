#!/usr/bin/env python
#--*--coding:UTF-8--*--

# Import modules
import socket
import sys
from datetime import datetime
import errno

# RAW_INPUT IP / HOST
remoteServer    = raw_input("Enter a remote host to scan: ")
remoteServerIP  = socket.gethostbyname(remoteServer)

# RAW_INPUT START PORT / END PORT
print "Please enter the range of ports you would like to scan on the machine"
startPort    = raw_input("Enter a start port: ")
endPort    = raw_input("Enter a end port: ")

print "Please wait, scanning remote host", remoteServerIP

#get Current Time as T1
t1 = datetime.now()

#Specify Range - From startPort to startPort
try:
    for port in range(int(startPort),int(endPort)):
		print ("Checking port {} ...".format(port))
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			print "Port {}: 	 Open".format(port)
		else:
			print "Port {}: 	 Closed".format(port)
			print "Reason:",errno.errorcode[result]
		sock.close()
# If interrupted 
except KeyboardInterrupt:
    print "You pressed Ctrl+C"
    sys.exit()
# If Host is wrong
except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()
# If server is down
except socket.error:
    print "Couldn't connect to server"
    sys.exit()
	
#get current Time as t2
t2 = datetime.now()
#total Time required to Scan
total =  t2 - t1
# Time for port scanning 
print 'Port Scanning Completed in: ', total