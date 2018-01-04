import json
from urllib.request import urlopen
import pprint

'''
Parse through all pages and place pages JSON into a list. Continue through all pages until the page has no data
'''
JSON_pages = []
y = 1
while True:
     html = urlopen('https://backend-challenge-summer-2018.herokuapp.com/challenges.json?id=1&page=' + str(y))
     y += 1
     data = html.read()
     decoded = data.decode('utf-8')
     JSON = json.loads(data.decode('utf-8'))
     if len(JSON['menus']) == 0:
          break
     else:
          JSON_pages.append(JSON)
     
     
'''
Parse through captured JSON data and place each node into the list Menus
'''
Menus = []
for x in range(0, len(JSON_pages)):
     z = True
     y = 0
     Menus.append([])
     while z == True:
          try:
               Menus[int(x)].append(JSON_pages[int(x)]['menus'][int(y)])
               y += 1
          except IndexError:
               z = False


test = {'menus': [] }

def p_print(data):
     pp = pprint.PrettyPrinter(indent=4)
     pp.pprint(data)
     
