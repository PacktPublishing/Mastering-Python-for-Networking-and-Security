import optparse, nmap
class NmapScanner:
     
    def __init__(self): 
        self.nmsc = nmap.PortScanner()
    
    def nmapScan(self, host, port): 
        self.nmsc.scan(host, port) 
        self.state = self.nmsc[host]['tcp'][int(port)]['state'] 
        print " [+] "+ host + " tcp/" + port + " " + self.state

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

    for port in ports: 
        NmapScanner().nmapScan(host, port)

if __name__ == "__main__": 
    main()