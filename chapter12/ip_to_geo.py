import requests

class IPtoGeo(object):

    def __init__(self, ip_address):
        # Initialize objects to store
        self.latitude = ''
        self.longitude = ''
        self.country = ''
        self.city = ''
        self.ip_address = ip_address
        self._get_location()

    def _get_location(self):
	
        json_request = requests.get('http://api.hostip.info/get_json.php?ip=%s&position=true' % self.ip_address).json()

        self.country = json_request['country_name']
        self.country_code = json_request['country_code']
        self.city = json_request['city']
        self.latitude = json_request['lat']
        self.longitude = json_request['lng']

if __name__ == '__main__':
    ip1 = IPtoGeo('8.8.8.8')
    print(ip1.__dict__)