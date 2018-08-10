#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import optparse, nmap
import json
import argparse


def callbackFTP(host, result):
        try:
                script = result['scan'][host]['tcp'][21]['script']
                
                print "Command line"+ result['nmap']['command_line']

                for key, value in script.items():
                        print 'Script {0} --> {1}'.format(key, value)
        except KeyError:
                # Key is not present
                pass
        

class NmapScannerAsyncFTP:
        
        def __init__(self):
                self.nmsync = nmap.PortScanner()
                self.nmasync = nmap.PortScannerAsync()
    
        def scanning(self):
                while self.nmasync.still_scanning():
                        self.nmasync.wait(5)    

        def nmapScanAsync(self, hostname, port):
                try:
                        print "Checking port "+ port +" .........."
                        
                        self.nmsync.scan(hostname, port)
                
                        self.state = self.nmsync[hostname]['tcp'][int(port)]['state']
                        print " [+] "+ hostname + " tcp/" + port + " " + self.state                            
  
                        #FTP
                        if (port=='21') and self.nmsync[hostname]['tcp'][int(port)]['state']=='open':
                                print 'Checking ftp port with nmap scripts......'
                                #scripts for ftp:21 open
                                print 'Checking ftp-anon.nse .....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p21 --script ftp-anon.nse",callback=callbackFTP)
                                self.scanning()
                                print 'Checking ftp-bounce.nse  .....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p21 --script ftp-bounce.nse",callback=callbackFTP)
                                self.scanning()
                                print 'Checking ftp-brute.nse  .....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p21 --script ftp-brute.nse",callback=callbackFTP)
                                self.scanning()
                                print 'Checking ftp-libopie.nse  .....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p21 --script ftp-libopie.nse",callback=callbackFTP)
                                self.scanning()
                                print 'Checking ftp-proftpd-backdoor.nse  .....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p21 --script ftp-proftpd-backdoor.nse",callback=callbackFTP)
                                self.scanning()
                                print 'Checking ftp-vsftpd-backdoor.nse   .....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p21 --script ftp-vsftpd-backdoor.nse",callback=callbackFTP)
                                self.scanning()
                                    
                except Exception,e:
                        print str(e)
                        print "Error to connect with " + hostname + " for port scanning" 
                        pass
        
    
    
    
if __name__ == "__main__":
        parser = argparse.ArgumentParser(description='Nmap scanner async')
            
        # Main arguments
        parser.add_argument("-target", dest="target", help="target IP / domain", required=True)
        parser.add_argument("-ports", dest="ports", help="Please, specify the target port(s) separated by comma[80,8080 by default]", default="80,8080")
    
        parsed_args = parser.parse_args()   

        port_list = parsed_args.ports.split(',')
    
        ip = parsed_args.target
    
        for port in port_list: 
                NmapScannerAsyncFTP().nmapScanAsync(ip, port)
        
