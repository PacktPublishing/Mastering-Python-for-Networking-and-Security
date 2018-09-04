import requests
import sys
from bs4 import BeautifulSoup, SoupStrainer

url = 'http://testphp.vulnweb.com/search.php?test=query'

data ={}

response = requests.get(url)

with open('XSS-attack-vectors.txt') as file:

	for payload in file:
	
		for field in BeautifulSoup(response.text, "html.parser",parse_only=SoupStrainer('input')):
			print(field)
			if field.has_attr('name'):
				if field['name'].lower() == "submit":
					data[field['name']] = "submit"
				else:
					data[field['name']] = payload

		response = requests.post(url, data=data)
		
		if payload in response.text:
			print("Payload "+ payload +" returned")
			
		data ={}