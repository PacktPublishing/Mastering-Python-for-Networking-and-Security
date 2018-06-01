import socket, time

host = 'localhost'
port = 1234

s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt (socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind ((host, port))
s.listen (5)

#recove address and port of the client
client, addr = s.accept ()
print addr
print "its has detected a connection from"
print client.getpeername ()
#Close customer socket
client.close ()
#close server socket
s.close ()
