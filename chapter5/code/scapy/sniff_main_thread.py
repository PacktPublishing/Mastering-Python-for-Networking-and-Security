from scapy.all import *

interface = "eth0"

def print_packet(packet):
	ip_layer = packet.getlayer(IP)
	print("[!] New Packet: {src} -> {dst}".format(src=ip_layer.src, dst=ip_layer.dst))

print("[*] Start sniffing...")
sniff(iface=interface, filter="ip", prn=print_packet)
print("[*] Stop sniffing")