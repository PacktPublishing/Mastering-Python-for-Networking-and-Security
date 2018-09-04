import socket
from geolite2 import geolite2
import argparse
import json

if __name__ == '__main__':
	# Commandline arguments
	parser = argparse.ArgumentParser(description='Get IP Geolocation info')
	parser.add_argument('--hostname', action="store", dest="hostname",required=True)

	# Parse arguments
	given_args = parser.parse_args()
	hostname = given_args.hostname
	ip_address = socket.gethostbyname(hostname)
	print("IP address: {0}".format(ip_address))

	# Call geolite2
	reader = geolite2.reader()
	response = reader.get(ip_address)
	print (json.dumps(response['continent']['names']['en'],indent=4))
	print (json.dumps(response['country']['names']['en'],indent=4))
	print (json.dumps(response['location']['latitude'],indent=4))
	print (json.dumps(response['location']['longitude'],indent=4))
	print (json.dumps(response['location']['time_zone'],indent=4))
