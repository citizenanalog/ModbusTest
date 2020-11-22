# importing the requests library
import requests
from pprint import pprint
# api-endpoint
r = requests.get('http://192.168.0.11/registers.cgi?address=1169')

pprint(r.json())