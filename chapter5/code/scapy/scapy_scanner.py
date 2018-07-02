
from scapy.all import *

#subnet scanner

for lsb in range(1,50):
	ip="192.168.1"+str(lsb)
	#request broadcast address
	arpRequest = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip,hwdst="ff:ff:ff:ff:ff:ff")
	arpResponse = srp1(arpRequest,timeout=1,verbose=0)
	if arpResponse:
		print "IP:"+arpResponse.psrc+"MAC:"+arpResponse.hwsrc