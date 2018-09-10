import urllib2

try:
	response = urllib2.urlopen("http://www.python.org")
	print(response.read())
	response.close()
except HTTPError, e:
	print e.code
except URLError, e:
	print e.reason