import urllib2
url = "http://www.python.org"
headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.117 Safari/537.36'}
request = urllib2.Request(url,headers=headers)
response = urllib2.urlopen(request)
# Here we check response headers
if response.code == 200: 
	print(response.headers)

