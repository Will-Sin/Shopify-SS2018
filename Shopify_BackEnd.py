'''
Version 1.3
'''

import json
from urllib.request import urlopen
import pprint

'''
Parse through all pages and place pages JSON into a list. Continue through all pages until the page has no data
'''
JSON_pages = []
y = 1
while True:
     html = urlopen('https://backend-challenge-summer-2018.herokuapp.com/challenges.json?id=2&page=' + str(y))
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
     while z == True:
          try:
               Menus.append(JSON_pages[int(x)]['menus'][int(y)])
               y += 1
          except IndexError:
               z = False

def recursion(tmp):
     '''
Function to go through current node ids (tmp) and adds new node id to tmp2 if it's parent id is in tmp.

Goes through cyclical function per id to check if cyclical or not. 

Checks if no more ids with parent id are left (check length of tmp2), if none left, you've found
the end of the menu
'''
     print(tmp)
     tmp2 = []
     for x in placeHolder['child']:
          if Menus[x-1]['parent_id'] in tmp:
               tmpMenu['children'].append(Menus[x-1]['id'])
               tmp2.append(Menus[x-1]['id'])
               cyclical(x)
     if len(tmp2)  == 0:
          return
     recursion(tmp2)
     return

def cyclical(x):
     '''
Checks if node's child id is less than itself, if so, we know node is cyclical.

Appends 1 to list c to notify that entire menu is cyclical.
'''
     if len(Menus[x-1]['child_ids']) > 0:
          for y in Menus[x-1]['child_ids']:
               if y < Menus[x-1]['id']:
                    c.append(1)

'''
Creates dictionary to seperate nodes that are parents, and nodes that are children. 
'''

placeHolder = {'parent': [], 'child': []}
for x in range(0, len(Menus)):
     if 'parent_id' in Menus[x]:
          placeHolder['child'].append(Menus[x]['id'])
     else:
          placeHolder['parent'].append(Menus[x]['id'])

'''
Goes through all parent ID's and checks every child node to connect them to it's parent ID.

Checks c list to see if cyclical or not. Refer to cyclical() function

Appends menu to final dictionary as either a valid or invalid menu.
'''
          
final = {'valid menus': [], 'invalid menus': []}
for x in placeHolder['parent']:
     tmpMenu= {'root_id': [x], 'children': []}
     tmp = [x]
     c = []
     recursion(tmp)
     if len(c) == 1:
          final['invalid menus'].append(tmpMenu)
     else:
          final['valid menus'].append(tmpMenu)
                    
def p_print(data):
     '''
list OR JSON is printed
'''
     pp = pprint.PrettyPrinter(indent=4)
     pp.pprint(data)

'''
def cyclical(child_ids):
     print(child_ids)
     if len(child_ids) > 1:
          for y in range(0, len(child_ids)):
               x = Menus[child_ids[y]]['child_ids']
               cyclical2([x[0]-1])
     if len(child_ids) == 0:
          print(1)
          return
     else:
          x = Menus[child_ids[0]]['child_ids']
          if len(x) == 0:
               print(3)
          if x[0] < child_ids[0]:
               print(2)
               return
          else:
               cyclical2([x[0]-1])
'''
