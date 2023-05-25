
import urllib.request
opener = urllib.request.build_opener()
response = opener.open("https://httpbin.org/get")
print(response.read())
import requests
response = requests.get('https://coinmarketcap.com/')
print(response.text)
response_pars = response.text.split('span>')


for elem in response_pars:
    if elem.startswith("$"):
        print(elem)