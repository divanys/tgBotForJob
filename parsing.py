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
print(dictNameAndLink)  # здесь будет 6 кнопок быстрого доступа

'''
Блок перехода по ссылке на конкретный товар из конкретной категории 
'''

urlHarryPotter = dictNameAndLink['ГАРРИ ПОТТЕР']

# print(urlHarryPotter)

lstForPriceLink, nameTextFor1Price = [], []

r = requests.get(urlHarryPotter).text
soup = BeautifulSoup(r, 'lxml')

allPrice = soup.find('ul', attrs={'class': 'products columns-3'})

# print(allPrice)

lstForPrice = allPrice.find_all('a', attrs={'class': 'ast-loop-product__link'})

for link in lstForPrice:
    lstForPriceLink.append(link.get('href'))


for name in range(len(lstForPrice)):
    nameTextFor1Price.append(lstForPrice[name].text)

dictPriceAndLinkTo = dict(zip(nameTextFor1Price, lstForPriceLink))

print(dictPriceAndLinkTo)
# print(nameTextFor1Price)
# print(len(nameTextFor1Price))
# print(len(lstForPriceLink))  # у нас должно получиться 6 элементов как и на сайте
# print(lstForPriceLink)


'''
Блок сбора информации на товар, а именно: 
1. Название
2. Фотография
3. Цена
4. Описание
5. аэаэаэаээа
'''

