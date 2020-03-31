import requests
import json
#site = requests.get('https://wp.pl')
data = requests.get('http://api.openrates.io/latest')
#print(site.text)
print(data.text)
data_str = data.text
data_json = data.json()
print(data_json)
print(data_json['rates']['PLN'])
data_json = json.loads(data_str)
print(data_json['rates']['PLN'])