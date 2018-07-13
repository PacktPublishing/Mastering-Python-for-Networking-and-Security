from pywebfuzz import fuzzdb
import requests

logins = fuzzdb.Discovery.PredictableRes.Logins

domain = "http://192.168.56.101"

for login in logins:
	print "Checking... "+ domain + login
	response = requests.get(domain + login)
	if response.status_code == 200:
		print "Login Resource: " +login
