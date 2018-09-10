import urllib2
import re

#enter url
web =  raw_input("Enter url: ")
#https://www.packtpub.com/books/info/packt/terms-and-conditions

#get response form url
response = urllib2.Request('http://'+web)

#get content page from response
content = urllib2.urlopen(response).read()

#regular expression
pattern = re.compile("[-a-zA-Z0-9._]+@[-a-zA-Z0-9_]+.[a-zA-Z0-9_.]+")

#get mails from regular expression
mails = re.findall(pattern,content)

print(mails)
