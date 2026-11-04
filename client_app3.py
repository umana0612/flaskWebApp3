import requests

from aiTools import response1

base_url = 'http://localhost:8080'

response1 = requests.get(f'{base_url}/cars/prices'.json())
response2 = requests.get(f'{base_url}/manufacturers'.json())
response3 = requests.get(f'{base_url}/cars/prices'.json())

print(response3)