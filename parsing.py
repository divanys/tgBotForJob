import requests
from bs4 import BeautifulSoup
import csv
from pandas import DataFrame


url = 'https://aliceandcat.ru/'
'''
Блок поиска и создания списка для, может быть, дополнительных категорий
'''

nameText, linkLink = [], []

r = requests.get(url).text
soup = BeautifulSoup(r, 'lxml')
navigatPanel = soup.find('div', attrs={'class': 'main-navigation ast-inline-flex'})

namePanel = navigatPanel.find_all('a', attrs={"class": "menu-link"})

for name in range(len(namePanel)):
    nameText.append(namePanel[name].text)

for link in namePanel:
    linkLink.append(link.get('href'))

# print(type(namePanel))
dictNameAndLink = dict(zip(nameText, linkLink))
# print()
# print(dictNameAndLink)

'''
Блок перехода по ссылке/ссылкам
'''

urlHarryPotter = dictNameAndLink['ГАРРИ ПОТТЕР']

# print(urlHarryPotter)

lstForPriceLink = []

r = requests.get(urlHarryPotter).text
soup = BeautifulSoup(r, 'lxml')

allPrice = soup.find('ul', attrs={'class': 'products columns-3'})

# print(allPrice)

lstForPrice = allPrice.find_all('div', attrs={'class': 'astra-shop-thumbnail-wrap'})

# print(lstForPrice)  # на некоторых нет скидки, поэтому выводит немного некрасиво, но элементов 6 штук - это правильно

for link in lstForPrice:
    lstForPriceLink.append(link.get('href'))

print(lstForPriceLink)