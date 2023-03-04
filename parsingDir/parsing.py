import requests
from bs4 import BeautifulSoup
import re

# print('*****************************************************')
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
priceLst, infoForPrice = [], []
photoLstLink, photoLst = [], []


for item in range(len(nameTextFor1Price)):
    urlFirstPrice = dictPriceAndLinkTo[keys[item]]


    r = requests.get(urlFirstPrice).text
    soup = BeautifulSoup(r, 'lxml')


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


    photo1 = soup.find_all('img', attrs={'class': 'wp-post-image'})

    for link in photo1:
        photoLstLink.append(link.get('src'))


    img = photoLstLink[item]
    p = requests.get(img)
    nameFile = f"parsingDir/img/{nameTextFor1Price[item]}.jpg".replace(' ', '')
    with open(nameFile, "wb") as file:
        file.write(p.content)    

    photoLst.append(nameFile)


'''
    Блок, где соединяются имеющиеся данные в словарь:
    {[товар[i]]: {[Название]: [название[i]], [Фотография]: [фото[i]], [Цена]: [цена[i]]}}
'''

countValues, valuesInfoPrice, information, infoAll = [], ['Название', 'Фотография', 'Цена'], [], dict()



for i in range(len(nameTextFor1Price)):
    countValues.append(i + 1)

for i in range(len(countValues)):
    information.append({'Название': f'{nameTextFor1Price[i]}', 'Фотография': f'{photoLst[i]}', 'Цена': f'{infoForPrice[i]}'})
    infoAll[countValues[i]] = information[i]

print(infoAll)

# print('*****************************************************')

keysALl = list(infoAll.keys())

# print(keys[0])

# print(infoAll[1]['Название'])

'''

{1: {'Название': 'Домик-конструктор Книжная Лавка “Wizarding Books” по мотивам вселенной  Гарри Поттера', 'Фотография': 'парсинг/img/Домик-конструкторКнижнаяЛавка“WizardingBooks”помотивамвселеннойГарриПоттера.jpg', 'Цена': '11990'}, 
 2: {'Название': 'Домик-конструктор Магазин Волшебных Палочек “Magic Wands Shop” по мотивам вселенной  Гарри Поттера', 'Фотография': 'парсинг/img/Домик-конструкторМагазинВолшебныхПалочек“MagicWandsShop”помотивамвселеннойГарриПоттера.jpg', 'Цена': '15990'},
 3: {'Название': 'Домик-конструктор Магазин Готового Платья “Ready-to-Wear Shop” по мотивам вселенной Гарри Поттера', 'Фотография': 'парсинг/img/Домик-конструкторМагазинГотовогоПлатья“Ready-to-WearShop”помотивамвселеннойГарриПоттера.jpg', 'Цена': '12990'}, 
 4: {'Название': 'Набор для создания домика Лесная Хижина по мотивам вселенной Гарри Поттера', 'Фотография': 'парсинг/img/НабордлясозданиядомикаЛеснаяХижинапомотивамвселеннойГарриПоттера.jpg', 'Цена': '17990'}, 
 5: {'Название': 'Набор для создания домика Мини-Магазин Волшебных Палочек “Magic Wands Shop” по мотивам вселенной Гарри Поттера', 'Фотография': 'парсинг/img/НабордлясозданиядомикаМини-МагазинВолшебныхПалочек“MagicWandsShop”помотивамвселеннойГарриПоттера.jpg', 'Цена': '8200'}, 
 6: {'Название': 'Домик-конструктор Совиная Лавка “Elliops Owl Emporium” по мотивам вселенной Гарри Поттера', 'Фотография': 'парсинг/img/Домик-конструкторСовинаяЛавка“ElliopsOwlEmporium”помотивамвселеннойГарриПоттера.jpg', 'Цена': '12990'}}

'''