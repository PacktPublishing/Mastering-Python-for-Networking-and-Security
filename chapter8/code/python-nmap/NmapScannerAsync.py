#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import optparse, nmap
import json
import argparse
  
def callbackMySql(host, result):
        try:
                script = result['scan'][host]['tcp'][3306]['script']
                
                print "Command line"+ result['nmap']['command_line']

                for key, value in script.items():
                        print 'Script {0} --> {1}'.format(key, value)
        except KeyError:
                # Key is not present
                pass
				
class NmapScannerAsync:
        
        def __init__(self):
                self.nmsync = nmap.PortScanner()
                self.nmasync = nmap.PortScannerAsync()
    
        def scanning(self):
                while self.nmasync.still_scanning():
                        self.nmasync.wait(5)    

        def nmapScan(self, hostname, port):
                try:
                        print "Checking port "+ port +" .........."
                        
                        self.nmsync.scan(hostname, port)
                
                        self.state = self.nmsync[hostname]['tcp'][int(port)]['state']
                        print " [+] "+ hostname + " tcp/" + port + " " + self.state                            

                        #mysql
                        if (port=='3306') and self.nmsync[hostname]['tcp'][int(port)]['state']=='open':
                                print 'Checking MYSQL port with nmap scripts......'
                                
                                #scripts for mysql:3306 open
                                print 'Checking mysql-audit.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p3306 --script mysql-audit.nse",callback=callbackMySql)
                                self.scanning()
                                print 'Checking mysql-brute.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p3306 --script mysql-brute.nse",callback=callbackMySql)
                                self.scanning()
                                print 'Checking mysql-databases.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p3306 --script mysql-databases.nse",callback=callbackMySql)
                                self.scanning()
                                print 'Checking mysql-databases.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p3306 --script mysql-dump-hashes.nse",callback=callbackMySql)
                                self.scanning()
                                print 'Checking mysql-dump-hashes.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p3306 --script mysql-empty-password.nse",callback=callbackMySql)
                                self.scanning()
                                print 'Checking mysql-enum.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p3306 --script mysql-enum.nse",callback=callbackMySql)
                                self.scanning()
                                print 'Checking mysql-info.nse".....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p3306 --script mysql-info.nse",callback=callbackMySql) 
                                self.scanning()
                                print 'Checking mysql-query.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p3306 --script mysql-query.nse",callback=callbackMySql)  
                                self.scanning()
                                print 'Checking mysql-users.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p3306 --script mysql-users.nse",callback=callbackMySql)  
                                self.scanning()
                                print 'Checking mysql-variables.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p3306 --script mysql-variables.nse",callback=callbackMySql) 
                                self.scanning()
                                print 'Checking mysql-vuln-cve2012-2122.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p3306 --script mysql-vuln-cve2012-2122.nse",callback=callbackMySql) 
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
                NmapScannerAsync().nmapScan(ip, port)
        
