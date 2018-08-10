#!/usr/bin/python

#import nmap module
import nmap

#initialize portScanner                       
nm = nmap.PortScanner()

# we ask the user for the host that we are going to scan
host_scan = raw_input('Host scan: ')
while host_scan == "":
    host_scan = raw_input('Host scan: ')

#execute scan in portlist
portlist="21,22,23,25,80,8080"	
nm.scan(hosts=host_scan, arguments='-n -p'+portlist)

#show nmap command
print nm.command_line()
hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]

#write in scan.txt file
file = open('scan.txt', 'w')
for host, status in hosts_list:
    print host, status
    file.write(host+'\n')

#show state for each port
array_portlist=portlist.split(',')
for port in array_portlist:
	state= nm[host_scan]['tcp'][int(port)]['state']
	print "Port:"+str(port)+" "+"State:"+state
	file.write("Port:"+str(port)+" "+"State:"+state+'\n')

#close file
file.close()