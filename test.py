import requests
# nameText, linkLink, newLst = ['a', 'b', 'c'], ['1', '2', '3'], ['py', 'th', 'on']
#
# lst = []
# for i in range(len(linkLink)):
#     lst.append({linkLink[i]: {nameText[i]: newLst[i]}})
#
# print(*lst, sep=', ')

img = 'https://aliceandcat.ru/wp-content/uploads/2021/04/f5d29b8db6c4a4d0e81c-600x900.jpg'
p = requests.get(img)
out = open("img.jpg", "wb")
out.write(p.content)
out.close()