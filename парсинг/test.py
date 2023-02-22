import requests
nameText, linkLink, newLst = ['a', 'b', 'c'], ['1', '2', '3'], ['py', 'th', 'on']

lst = []
for i in range(len(linkLink)):
    lst.append({linkLink[i]: {nameText[i]: newLst[i]}})

print(lst)
