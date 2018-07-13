# -*- encoding: utf-8 -*-
import dns
import dns.resolver
import dns.query 
import dns.zone 
import dns.name
import dns.reversename
import sys

if len(sys.argv) != 2:
    print "[-] usage python DNSPythonExample.py <domain_name>"
    sys.exit()

domain = sys.argv[1]

ansIPV4,ansMX,ansNS,ansIPV6=(dns.resolver.query(domain,'A'),
                          dns.resolver.query(domain,'MX'),
                          dns.resolver.query(domain, 'NS'), 
                          dns.resolver.query(domain, 'AAAA'))


print('Name Servers: %s' % ansNS.response.to_text())
print('Name Servers: %s' %[x.to_text() for x in ansNS])

print('Ipv4 addresses: %s' %[x.to_text() for x in ansIPV4])
print('Ipv4 addresses: %s' % ansIPV4.response.to_text())

print('Ipv6 addresses: %s' %[x.to_text() for x in ansIPV6])
print('Ipv6 addresses: %s' % ansIPV6.response.to_text())

print('Mail Servers: %s' % ansMX.response.to_text())
for data in ansMX:
	print('Mailserver', data.exchange.to_text(), 'has preference', data.preference)




