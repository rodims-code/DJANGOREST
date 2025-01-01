import requests

endpoint = 'http://httpbin.org/anything'
response = requests.get(endpoint, json={'Bonjour':'Hello'})
print(response.text)

{'args': {}, 'data': '', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.32.3', 'X-Amzn-Trace-Id': 'Root=1-67749711-463af5d2079b7bc51777113c'}, 'json': None, 'method': 'GET', 'origin': '197.214.196.54', 'url': 'http://httpbin.org/anything'}

{
  "args": {}, 
  "data": "", 
  "files": {},
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.32.3",
    "X-Amzn-Trace-Id": "Root=1-67749794-3e085db87d4c854f7de481bf"
  },
"""   "json": null, """
  "method": "GET",
  "origin": "197.214.196.54",
  "url": "http://httpbin.org/anything"
}