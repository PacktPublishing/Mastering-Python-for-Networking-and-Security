import urllib2
response = urllib2.urlopen("http://www.packtpub.com/networking-and-servers/mastering-python-networking-and-security")
response.geturl()
response.getcode()
response.headers.keys()
response.headers.values()
for header,value in response.headers.items():
	print(header + ":" + value)