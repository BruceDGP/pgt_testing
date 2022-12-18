import requests

response = requests.get('https://httpbin.org/get')

response.status_code

def check(resp):
    if resp:
        return True
    else
        return True

check(response)