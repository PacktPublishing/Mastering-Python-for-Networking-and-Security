#!/usr/bin/python

import pcapy

devs = pcapy.findalldevs()
print(devs)

#  device, # of byte to capture per packet, promiscuous mode, timeout (ms)
cap = pcapy.open_live("eth0", 65536 , 1 , 0)

count = 1
while count:
    (header, payload) = cap.next()
    print(count)
    count = count + 1
