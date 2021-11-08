import requests

API_TOKEN = '06f1836af2a649bd71b2caa2c91fd336'
API_URL = 'http://api.ipstack.com'

def fetch_details_for_ip(ipaddress):
    data = requests.get(f'{API_URL}/{ipaddress}?access_key={API_TOKEN}&output=json').json()
    details = dict()
    details['ipaddress'] = ipaddress
    details['latitude'] = str(data['latitude'])
    details['longitude'] = str(data['longitude'])
    details['city'] = str(data['city'])
    details['zip'] = str(data['zip'])
    return details