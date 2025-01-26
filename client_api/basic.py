import requests

endpoint = "http://httpbin.org/status/product"

response = requests.get(endpoint)
print(response.text)