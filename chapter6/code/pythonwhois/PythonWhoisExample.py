# -*- encoding: utf-8 -*-
'''
Notas:
Lib: https://pypi.python.org/pypi/pythonwhois
'''
import pythonwhois
import sys

if len(sys.argv) != 2:
    print "[-] usage python PythonWhoisExample.py <domain_name>"
    sys.exit()

print sys.argv[1]
whois = pythonwhois.get_whois(sys.argv[1])
for key in whois.keys():
    print "[+] %s : %s \n" %(key, whois[key])
	

whois = pythonwhois.net.get_root_server(sys.argv[1])
print whois

whois = pythonwhois.net.get_whois_raw(sys.argv[1])
print whois