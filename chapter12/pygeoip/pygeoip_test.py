# -*- coding: UTF-8 -*-
 
import pygeoip
 
def main():
    geoip_country() 
    geoip_city()
 
def geoip_city():
    path = 'GeoLiteCity.dat'
    gic = pygeoip.GeoIP(path)
    print(gic.record_by_addr('64.233.161.99'))
    print(gic.record_by_name('google.com'))
    print(gic.region_by_name('google.com'))
    print(gic.region_by_addr('64.233.161.99'))
 
def geoip_country(): 
    path = 'GeoIP.dat'
    gi = pygeoip.GeoIP(path)
    print(gi.country_code_by_name('google.com'))
    print(gi.country_code_by_addr('64.233.161.99'))
    print(gi.country_name_by_name('google.com'))
    print(gi.country_name_by_addr('64.233.161.99'))

if __name__ == '__main__':
    main()
