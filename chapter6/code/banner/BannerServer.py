import socket
import argparse
import re

parser = argparse.ArgumentParser(description='Get banner server')

# Main arguments
parser.add_argument("-target", dest="target", help="target IP", required=True)
parser.add_argument("-port", dest="port", help="port", type=int, required=True)
parsed_args = parser.parse_args()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((parsed_args.target, parsed_args.port))
sock.settimeout(2)

http_get = b"GET / HTTP/1.1\nHost: "+parsed_args.target+"\n\n"
data = ''
try:
	sock.sendall(http_get)
	data = sock.recvfrom(1024)
	data = data[0]
	print data
	
	headers = data.splitlines()
	#  use regular expressions to look for server header
	for header in headers:
		if re.search('Server:', header):
			print(header)

except socket.error:
	print ("Socket error", socket.errno)
finally:
	sock.close()
		