import requests

endpoint = "http://127.0.0.1:8000/api/"

response = requests.get(endpoint, params={'abc':123}, json={'query': '{name, age, language}'})
print(response.json())
print(response.status_code)
""" {
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.32.3",
    "X-Amzn-Trace-Id": "Root=1-67a9f921-3d5a541e4af20e4d7d057c11"
  },
  "json": null,
  "method": "GET",
  "origin": "102.129.82.97",
  "url": "http://httpbin.org/anything"
} """