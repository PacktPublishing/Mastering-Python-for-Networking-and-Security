#!/usr/bin/python
import sys
from scapy.all import *
p=IP(dst='www.google.es')/ICMP()
send(p)

