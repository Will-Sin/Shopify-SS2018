import json
from urllib.request import urlopen

html = urlopen('https://backend-challenge-summer-2018.herokuapp.com/challenges.json?id=1&page=1')

data = html.read()
decoded = data.decode('utf-8')

JSON = json.loads(decoded)

'''
Parse through captured JSON data and place each node into the list Menus
'''
Menus = []
x = True
y = 0
while x == True:
     try:
          Menus.append(JSON['menus'][int(y)])
          y += 1
     except IndexError:
          x = False
s

test = {'menus':}
