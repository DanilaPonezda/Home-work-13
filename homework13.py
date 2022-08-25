import requests
from bs4 import BeautifulSoup

link ="https://ru.wikipedia.org/wiki/%D0%98%D1%81%D0%BF%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D1%81%D1%82%D1%8B%D0%B4"
res = requests.get(link)
soup = BeautifulSoup(res.text, "lxml")

name = soup.find_all("div", class_="noprint")

print(name)

for i in name:
    print(i.text)