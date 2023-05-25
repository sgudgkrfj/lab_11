"""import urllib.request
opener = urllib.request.build_opener()
response = opener.open("https://httpbin.org/get")
print(response.read())"""

import  requests
response = requests.get('https://coinmarketcap.com/')

from bs4 import BeautifulSoup
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find("title").text
    print(title)
else:
    print("Немає підключення ", response.status_code)







