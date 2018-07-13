#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shodan
import re

sites =[]

shodanKeyString = 'v4YpsPUJ3wjDxEqywwu6aF5OZKWj8kik'

shodanApi = shodan.Shodan(shodanKeyString)

results = shodanApi.search("port: 21 Anonymous user logged in")
print "hosts number: " + str(len( results['matches']))
for match in results['matches']:
	if match['ip_str'] is not None:
		print match['ip_str']
		sites.append(match['ip_str'])
