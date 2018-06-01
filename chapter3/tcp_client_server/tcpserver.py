#!/usr/bin/python
# tcpserver.py

import socket
import threading

bind_ip   = "127.0.0.1"
bind_port = 9999

#  family = Internet, type = stream socket means TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#  we have a socket, we need to bind to an IP address and port
#  to have a place to listen on
server.bind((bind_ip,bind_port))

server.listen(5)

print "[*] Server Listening on %s:%d" % (bind_ip,bind_port)

# this is our client handling thread
def handle_client(client_socket):

    # just print out what the client sends
    request = client_socket.recv(1024)
    
    print "[*] Received: %s" % request    

    client_socket.send("ACK!")
	
	#print information about client connected
    print client_socket.getpeername()
    client_socket.close()


while True:

    client,addr = server.accept()
    
    print "[*] Accepted connection from: %s:%d" % (addr[0],addr[1])

    # spin up our client thread to handle incoming data
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()


