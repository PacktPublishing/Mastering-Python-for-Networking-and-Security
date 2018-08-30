import shodan
import socket

SHODAN_API_KEY = "v4YpsPUJ3wjDxEqywwu6aF5OZKWj8kik"

api = shodan.Shodan(SHODAN_API_KEY)


# Wrap the request in a try/ except block to catch errors
try:
	# Search Shodan OpenSSL/1.0.1
	results = api.search('OpenSSL/1.0.1')
	
	# Show the results
	print('Total Vulnerable servers: %s' % results['total'])
	
	for result in results['matches']:
		print('IP: %s' % result['ip_str'])
		print('Hostname: %s' % socket.getfqdn(result['ip_str']))
		print(result['data'])
		
except shodan.APIError as e:
        print('Error: %s' % e)
