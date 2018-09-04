#coding: utf-8
#!/usr/local/bin/python

import pygeoip
import pprint

gi = pygeoip.GeoIP('GeoLiteCity.dat')

pprint.pprint("Country code: %s "%(str(gi.country_code_by_addr('173.194.34.192'))))
pprint.pprint("Country code: %s "%(str(gi.country_code_by_name('google.com'))))
pprint.pprint("Country name: %s "%(str(gi.country_name_by_addr('173.194.34.192'))))
pprint.pprint("Country code: %s "%(str(gi.country_name_by_name('google.com'))))

gi2 = pygeoip.GeoIP('GeoIPASNum.dat')

pprint.pprint("Organization by addr: %s "%(str(gi2.org_by_addr('173.194.34.192'))))
pprint.pprint("Organization by name: %s " %(str(gi2.org_by_name('google.com'))))

for record,value in gi.record_by_addr('173.194.34.192').items():
	print(record + "-->" + str(value))



