import dns.reversename

name = dns.reversename.from_address("99.17.217.172")

print name

print dns.reversename.to_address(name)



