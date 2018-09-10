import urllib2
url = raw_input("Enter the URL ")
http_response = urllib2.urlopen(url)
print 'Status Code: '+ str(http_response.code)
if http_response.code == 200: 
	print(http_response.headers)
