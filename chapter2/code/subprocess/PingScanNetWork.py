#!/usr/bin/env python
from subprocess import Popen, PIPE
import sys
import argparse

parser = argparse.ArgumentParser(description='Ping Scan Network')
    
# Main arguments
parser.add_argument("-network", dest="network", help="NetWork segment[For example 192.168.56]", required=True)
parser.add_argument("-machines", dest="machines", help="Machines number",type=int, required=True)

parsed_args = parser.parse_args()    
    
for ip in range(1,parsed_args.machines+1):
	ipAddress = parsed_args.network +'.' + str(ip)
	print "Scanning %s " %(ipAddress)
	if sys.platform.startswith('linux'):
		# Linux
		subprocess = Popen(['/bin/ping', '-c 1 ', ipAddress], stdin=PIPE, stdout=PIPE, stderr=PIPE)
	elif sys.platform.startswith('win'):
		# Windows
		subprocess = Popen(['ping', ipAddress], stdin=PIPE, stdout=PIPE, stderr=PIPE)
	stdout, stderr= subprocess.communicate(input=None)
	print stdout
	if "Lost = 0" in stdout or "bytes from " in stdout:
		print "The Ip Address %s has responded with a ECHO_REPLY!" %(stdout.split()[1])
