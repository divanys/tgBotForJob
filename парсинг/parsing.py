import requests
from bs4 import BeautifulSoup
import csv
from pandas import DataFrame
import re

print('*****************************************************')
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

dictNameAndLink = dict(zip(nameText, linkLink))

'''
Блок перехода по ссылке на конкретный товар из конкретной категории 
'''

urlHarryPotter = dictNameAndLink['ГАРРИ ПОТТЕР']

lstForPriceLink, nameTextFor1Price = [], []

r = requests.get(urlHarryPotter).text
soup = BeautifulSoup(r, 'lxml')

allPrice = soup.find('ul', attrs={'class': 'products columns-3'})

lstForPrice = allPrice.find_all('a', attrs={'class': 'ast-loop-product__link'})

for link in lstForPrice:
    lstForPriceLink.append(link.get('href'))


for name in range(len(lstForPrice)):
    nameTextFor1Price.append(lstForPrice[name].text)

dictPriceAndLinkTo = dict(zip(nameTextFor1Price, lstForPriceLink))


'''
Блок сбора информации на товар, а именно: 
    1. Цена
    2. Фотография
    3. Название у нас имеется в предыдущем блоке в массиве nameTextFor1Price и в словаре с указанием ссылки на продукт
    (4. Ссылка на оплату - это будет с платёжкой)
'''

# Сейчас делаю по 1 элементу, но надо будет обернуть в цикл для всех остальных объектов

keys = list(dictPriceAndLinkTo.keys())
firstPrice = keys[0]
urlFirstPrice = dictPriceAndLinkTo[keys[0]]


r = requests.get(urlFirstPrice).text
soup = BeautifulSoup(r, 'lxml')


'''
    1. Блок парсинга цены
'''
priceLst, infoForPrice = [], []
priceProduct = soup.find_all('span', attrs={'class': 'woocommerce-Price-amount amount'})

# у нас имеется 2 цены и каждая цена на сайте аааааааааааа расположена по одинаковым тегам и классааааааааам аааааааааа
# а ещё не у всех товаров есть скидка
# здесь создаётся массив из обеих цен и выборка лишь цифр, в конце в priceCurrent передаётся последняя по индексу цена

priceAll = [i.text for i in priceProduct]
for i in range(len(priceAll)):
    price = re.findall(r'\d+', priceAll[i])
    priceLst.append(''.join(price))

priceCurrent = priceLst[-1]
infoForPrice.append(priceCurrent)

'''
    2. Блок парсинга фотографии
'''

photoLstLink, photoLst = [], []
photo1 = soup.find_all('img', attrs={'class': 'wp-post-image'})

for link in photo1:
    photoLstLink.append(link.get('src'))


img = photoLstLink[0]
p = requests.get(img)
nameFile = f"парсинг/img/{nameTextFor1Price[0]}.jpg"
with open(nameFile, "wb") as file:
    file.write(p.content)    

photoLst.append(nameFile)


'''
    Блок, где соединяются имеющиеся данные в словарь:
    {[товар[i]]: {[Название]: [название[i]], [Фотография]: [фото[i]], [Цена]: [цена[i]]}}
'''

countValues, valuesInfoPrice, information = [], ['Название', 'Фотография', 'Цена'], dict()



for i in range(len(nameTextFor1Price)):
    countValues.append(i + 1)

for i in range(len(countValues)):
    information[countValues[i]] = 'kkk'
print(information)

print('*****************************************************')

# dictionary_name[key] = value