#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shodan
import re


class ShodanSearch:
    """ Class for search in Shodan """
    def __init__(self,API_KEY):
        self.api =  shodan.Shodan(API_KEY)    

    def search(self,search):
        """ Search from the search string"""
        try:
            result = self.api.search(str(search))
            return result
        except Exception as e:
            print 'Exception: %s' % e
            result = []
            return result

        
    def get_host_info(self,IP):
        """ Get the information that may have shodan on an IP"""
        try:
                host = self.api.host(IP)
                return host
        except Exception as e:
                print 'Exception: %s' % e
                host = []
                return host     


def usage():
    print """ShodanSearch.py {OPTION} {SEARCH_STRING | HOST}
     OPCIONES:
      -s, --search: To search according to a certain string
      -h, --host: To obtain the information of a host according to IP address
     Examples
      ShodanSearch.py -s apache
      ShodanSearch.py -h 8.8.8.8"""

def banner():
        print """
         ____  _               _             _____      
                / ___|| |__   ___   __| | __ _ _ __
                \___ \| '_ \ / _ \ / _` |/ _` | '_ \  
                 ___) | | | | (_) | (_| | (_| | | | |  
                |____/|_| |_|\___/ \__,_|\__,_|_| |_|
                                               Search
    """ 

def main():
    import sys
    import time

    API_KEY = 'v4YpsPUJ3wjDxEqywwu6aF5OZKWj8kik'
    shodan = ShodanSearch(API_KEY)
    if len(sys.argv) < 3:
        usage()
        sys.exit(2)
    else:
        if sys.argv[1] == '-s' or sys.argv[1] == '--search':
            banner()
            time.sleep(3)
            result = shodan.search(sys.argv[2])
            if len(result) != 0:
                    print 'Quantity of results found: %s' % result['total']
                    for i in result['matches']:
                        print 'City: %s' % i.get('city','Unknown')
                        print 'Country: %s' % i.get('country_name','Unknown')
                        print 'IP: %s' % i.get('ip_str')
                        print 'O.S: %s' % i.get('os','Unknown')
                        print 'Port: %s' % i.get('port')
                        print 'Hostnames: %s' % i.get('hostnames')
                        print 'Latitude: %s' % i.get('latitude','Unknown')
                        print 'Longitude: %s' % i.get('longitude','Unknown')
                        print 'Updated: %s' % i.get('updated')
                        print i['data']
                        print ''
                    print result.keys()
                    if 'organizations' in result.keys():
                        for key,value in result['organizations'].items():
                            print key + ":" + value
                    if 'countries' in result.keys():
                        for key,value in result['countries'].items():
                            print key + ":" + value
                    if 'cities' in result.keys():
                        for key,value in result['cities'].items():
                            print key + ":" + value                        
                        
        elif sys.argv[1] == '-h' or sys.argv[1] == '--host':
            banner()
            time.sleep(3)
            host = shodan.get_host_info(sys.argv[2])
            if len(host) != 0:
				#print host
				# printing the information about the host
				if 'ip' in host.keys():
					print 'IP: %s' % host.get('ip_str')
				if 'country_name' in host.keys():
					print 'Country: %s' % host.get('country_name','Unknown')
				if 'country_code' in host.keys():
					print 'Country code: %s' % host.get('country_code','Unknown')
				if 'city' in host.keys():
					print 'City: %s' % host.get('city','Unknown')
				if 'isp' in host.keys():
					print 'ISP: %s' % host.get('isp','Unknown')
				if 'latitude' in host.keys():
					print 'Latitude: %s' % host.get('latitude')
				if 'longitude' in host.keys():
					print 'Longitude: %s' % host.get('longitude')
				if 'hostnames' in host.keys():
					print 'Hostnames: %s' % host.get('hostnames')
                # print banners
				try:
					for i in host['data']:
						print 'Port: %s' % i['port']
						print 'Banner: %s' % i['banner']
						print ''
				except Exception,e:
					pass
        else:
                    usage()
                    sys.exit(2)

if __name__ == '__main__':
    main()
