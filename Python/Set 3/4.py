import requests
from bs4 import BeautifulSoup
page = requests.get("https://www.w3schools.com/xml/simple.xml")
soup = BeautifulSoup(page.content,'lxml')
food = soup.find_all('food')
for each in food:
    print(soup.find('name').get_text())
    print(soup.find('price').get_text())
    print(soup.find('description').get_text())
    print(soup.find('calories').get_text())