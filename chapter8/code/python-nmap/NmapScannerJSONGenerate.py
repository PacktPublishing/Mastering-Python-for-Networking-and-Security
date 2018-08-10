#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import optparse, nmap
import json

class NmapScannerJSONGenerate:
     
    def __init__(self):
        self.nmsc = nmap.PortScanner()
    
    def nmapScan(self, host, port):
        try:
            print "Checking port "+ port +" .........."
            self.nmsc.scan(host, port)
            
            # Command info
            print "[*] Execuing command: %s" % self.nmsc.command_line()     
            self.state = self.nmsc[host]['tcp'][int(port)]['state']
            print " [+] "+ host + " tcp/" + port + " " + self.state
            print self.nmsc[host].tcp(int(port))
            self.server = self.nmsc[host].tcp(int(port))['product']
            self.version = self.nmsc[host].tcp(int(port))['version']
            print " [+] "+ self.server + " " + self.version + " tcp/" + port
            
        except Exception,e:
            print "Error to connect with " + host + " for port scanning" 
            pass
        
    
    def nmapScanJSONGenerate(self, host, ports):
        try:
            print "Checking ports "+ str(ports) +" .........."
            self.nmsc.scan(host, ports)
            
            # Command info
            print "[*] Execuing command: %s" % self.nmsc.command_line()
            
            print self.nmsc.csv()
            results = {}     
            
            for x in self.nmsc.csv().split("\n")[1:-1]:
                splited_line = x.split(";")
                host = splited_line[0]
                proto = splited_line[1]
                port = splited_line[2]
                state = splited_line[4]
                
                try:
                    if state == "open":
                        results[host].append({proto: port})
                except KeyError:
                    results[host] = []
                    results[host].append({proto: port})
                
            # Store info
            file_info =  "scan_%s.json" % host
            with open(file_info, "w") as file_json:
                json.dump(results, file_json)
                
            print "[*] File '%s' was generated with scan results" % file_info            
    
        except Exception,e:
            print e
            print "Error to connect with " + host + " for port scanning" 
            pass
    
def main():
    parser = optparse.OptionParser("usage%prog " + "-H <target host> -p <target port>") 
    parser.add_option('-H', dest = 'host', type = 'string', help = 'Please, specify the target host.')
    parser.add_option('-p', dest = 'ports', type = 'string', help = 'Please, specify the target port(s) separated by comma.')
    (options, args) = parser.parse_args()
    if (options.host == None) | (options.ports == None): 
        print '[-] You must specify a target host and a target port(s).'
        exit(0)
    host = options.host
    ports = options.ports.split(',')

    NmapScannerJSONGenerate().nmapScanJSONGenerate(host,ports)

if __name__ == "__main__": 
    main()
            