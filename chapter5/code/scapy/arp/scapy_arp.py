#! /usr/bin/env python

import sys
from scapy.all import sr1,IP,ICMP

#take an IP or a name as first parameter, send an ICMP echo request packet and display the completely dissected return packet.
 
p=sr1(IP(dst=sys.argv[1])/ICMP())
if p:
    p.show()