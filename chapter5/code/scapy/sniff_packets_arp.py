from scapy.all import *

def arpDisplay(pkt):
	if pkt[ARP].op == 1: #request
		x= "Request: {} is asking about {} ".format(pkt[ARP].psrc,pkt[ARP].pdst)
		print x
	if pkt[ARP].op == 2: #response
		x = "Response: {} has address {}".format(pkt[ARP].hwsrc,pkt[ARP].psrc)
		print x

sniff(prn=arpDisplay, filter="ARP", store=0, count=10)
