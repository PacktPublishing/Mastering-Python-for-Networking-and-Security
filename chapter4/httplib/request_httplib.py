import httplib

connection = httplib.HTTPConnection("www.packtpub.com")
connection.request("GET", "/networking-and-servers/mastering-python-networking-and-security")
response = connection.getresponse()
print response
print response.status, response.reason
data = response.read()
print data
