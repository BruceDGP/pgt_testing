import requests

response = requests.get('https://httpbin.org/get')

response.status_code