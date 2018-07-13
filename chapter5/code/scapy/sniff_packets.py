#import scapy module to python
from scapy.all import *
 
# custom custom packet sniffer action method
def sniffPackets(packet):
	if packet.haslayer(IP):
		pckt_src=packet[IP].src
		pckt_dst=packet[IP].dst
		pckt_ttl=packet[IP].ttl
		print "IP Packet: %s is going to %s and has ttl value %s" (pckt_src,pckt_dst,pckt_ttl)
 
def main():
	print "custom packet sniffer"
	#call scapy’s sniff method
	sniff(filter="ip",iface="wlan0",prn=sniffPackets)
 
if __name__ == '__main__':
	main()
