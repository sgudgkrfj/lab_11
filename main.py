import  requests
from bs4 import BeautifulSoup
response = requests.get('https://www.example.com/')

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find('title').text
    print(title)
else:
    print("Немає підключення ", response.status_code)