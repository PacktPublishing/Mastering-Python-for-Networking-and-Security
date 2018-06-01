#!/usr/bin/python
# tcpclient.py
 
import socket

host="127.0.0.1"
port = 9999

try:
	mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	mysocket.connect((host, port))
	print 'Conntencted to host '+str(host)+' in port: '+str(port)
	message = mysocket.recv(1024)
	print "Received", message
	while True:
		message = raw_input("> ")
		mysocket.send(message)
		if message== "quit":
			break
except socket.errno as e:
	print("Socket error ", e)
finally:
	mysocket.close()