import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/quote/BTC-USD/"


response = requests.get(url)

print(response)
print(response.status_code == 200)

t = response.text
soup = BeautifulSoup(t, features='html.parser')

finalName = "Volume (24hr) All Currencies"
lis = soup.find_all("li", class_="svelte-tx3nkj")

nameVal = {}
for li in lis:
    name = ""
    val = ""
    for i in range(len(li.find_all("span"))):
        if i == 0:
            name = li.find_all("span")[i].text
        if i == 1:
            val = li.find_all("span")[i].text
        nameVal[name] = val
        
print(nameVal)
    