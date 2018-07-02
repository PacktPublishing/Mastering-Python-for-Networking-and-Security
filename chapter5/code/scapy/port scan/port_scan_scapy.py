from scapy.all import sr1, IP, TCP

OPEN_PORTS = []

def analyze_port(host, port):
	"""
    Function that determines the status of a port: Open / closed
    :param host: target
    :param port: port to test
    :type port: int
	"""
  
    print "[ii] Scanning port %s" % port
    res = sr1(IP(dst=host)/TCP(dport=port), verbose=False, timeout=0.2)
    if res is not None and TCP in res:
		if res[TCP].flags == 18:
                	OPEN_PORTS.append(port)
                	print "Port  %s open " % port


def main():
    for x in xrange(0, 80):
        analyze_port("domain", x)
    print "[*] Ports openned:"
    for x in OPEN_PORTS:
        print " - %s/TCP" % x
        
