#!/usr/bin/python

import pcapy
from struct import *

pcap_file = pcapy.open_offline("file.pcap")
count = 1

while count:
    print("Packet #: ", count)
    count = count + 1
    (header,payload) = pcap_file.next()
    l2hdr = payload[:14]
    l2data = unpack("!6s6sH", l2hdr)
    srcmac = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(l2hdr[0]), ord(l2hdr[1]), ord(l2hdr[2]), ord(l2hdr[3]), ord(l2hdr[4]), ord(l2hdr[5]))
    dstmac = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(l2hdr[6]), ord(l2hdr[7]),   ord(l2hdr[8]), ord(l2hdr[9]), ord(l2hdr[10]), ord(l2hdr[11]))
    print("Source MAC: ", srcmac, " Destination MAC: ", dstmac)

	# get IP header, which is 20 bytes long
	# then unpack it into what it is
    ipheader = unpack('!BBHHHBBH4s4s' , payload[14:34])
    timetolive = ipheader[5]
    protocol = ipheader[6]
    print("Protocol ", str(protocol), " Time To Live: ", str(timetolive))
