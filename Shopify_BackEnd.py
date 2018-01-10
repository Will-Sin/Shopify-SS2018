'''
Version 1.6
'''

import json
from urllib.request import urlopen
import pprint

'''
Parse through all pages and place pages JSON into a list. Continue through all pages until the page has no data
'''
json_pages = []
html = urlopen('https://backend-challenge-summer-2018.herokuapp.com/challenges.json?id=1&page=1')
raw_html = html.read()
json_clean = json.loads(raw_html.decode('utf-8'))
json_per_page = json_clean['pagination']['per_page']
json_page_total = json_clean['pagination']['total']
num_data_pages = int(json_page_total/json_per_page)
for x in range(1, num_data_pages+1):
     html = urlopen('https://backend-challenge-summer-2018.herokuapp.com/challenges.json?id=1&page=' + str(x))
     raw_html = html.read()
     json_clean = json.loads(raw_html.decode('utf-8'))
     json_pages.append(json_clean)
     
'''
Parse through captured JSON data and place each node into the list Menus
'''
menus = []
for x in range(0, len(json_pages)):
     z = True
     y = 0
     while z == True:
          try:
               menus.append(json_pages[int(x)]['menus'][int(y)])
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
     for x in place_holder['child']:
          if menus[x-1]['parent_id'] in tmp:
               tmp_menu['children'].append(menus[x-1]['id'])
               tmp2.append(menus[x-1]['id'])
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
     if len(menus[x-1]['child_ids']) > 0:
          for y in menus[x-1]['child_ids']:
               if y < menus[x-1]['id']:
                    c.append(1)

'''
Creates dictionary to seperate nodes that are parents, and nodes that are children. 
'''

place_holder = {'parent': [], 'child': []}
for x in range(0, len(menus)):
     if 'parent_id' in menus[x]:
          place_holder['child'].append(menus[x]['id'])
     else:
          place_holder['parent'].append(menus[x]['id'])

'''
Goes through all parent ID's and checks every child node to connect them to it's parent ID.

Checks c list to see if cyclical or not. Refer to cyclical() function

Appends menu to final dictionary as either a valid or invalid menu.
'''
          
final = {'valid menus': [], 'invalid menus': []}
for x in place_holder['parent']:
     tmp_menu= {'root_id': [x], 'children': []}
     tmp = [x]
     c = []
     recursion(tmp)
     if len(c) > 0:
          final['invalid menus'].append(tmp_menu)
     else:
          final['valid menus'].append(tmp_menu)
                    
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
