import requests

response = requests.get('https://httpbin.org/get')

response.status_code

def check(resp):
    if resp:
        print(resp.status_code)
        return resp.status_code
    else:
        return resp.status_code

check(response)
response.status_code