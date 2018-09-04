# -*- encoding: utf-8 -*-

import pprint
from pygeocoder import Geocoder

results = Geocoder.geocode("Mountain View")
pprint.pprint(results.coordinates)
pprint.pprint(results.country)
pprint.pprint(results.postal_code)
print(results.latitude)
print(results.longitude)

results = Geocoder.reverse_geocode(results.latitude, results.longitude)
pprint.pprint(results.formatted_address)
