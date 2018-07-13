from pywebfuzz import fuzzdb
import requests

httpMethods= fuzzdb.attack_payloads.http_protocol.http_protocol_methods

domain = "http://www.google.com"

for method in httpMethods:
	print "Probando... "+ domain +"/"+ method
	response = requests.get(domain, method)
	if response.status_code not in range(400,599):
		print " Method Allowed: " + method