'''
Version 1.8
'''

import json
from urllib.request import urlopen
import pprint

def main():
     for i in range(1, 3):
          json_pages2 = json_pages1(int(i))
          json_menus2 = json_menus1(json_pages2)
          place_holder2 = place_holder1(json_menus2)
          json_final2 = json_final1(place_holder2, json_menus2)
          p_print(json_final2)

def json_pages1(id):
     '''
     Parse through all pages and place pages JSON into a list. Continue through all pages until the page has no data
     '''
     json_pages = []
     html = urlopen('https://backend-challenge-summer-2018.herokuapp.com/challenges.json?id=' + str(id) + '&page=1')
     raw_html = html.read()
     json_clean = json.loads(raw_html.decode('utf-8'))
     json_per_page = json_clean['pagination']['per_page']
     json_page_total = json_clean['pagination']['total']
     num_data_pages = int(json_page_total/json_per_page)
     for x in range(1, num_data_pages+1):
          html = urlopen('https://backend-challenge-summer-2018.herokuapp.com/challenges.json?id=' + str(id) + '&page=' + str(x))
          raw_html = html.read()
          json_clean = json.loads(raw_html.decode('utf-8'))
          json_pages.append(json_clean)
     return json_pages
     

def json_menus1(json_pages):
     '''
     Parse through captured JSON data and place each node into the list Menus
     '''
     json_menus = []
     for x in range(0, len(json_pages)):
          z = True
          y = 0
          while z == True:
               try:
                    json_menus.append(json_pages[int(x)]['menus'][int(y)])
                    y += 1
               except IndexError:
                    z = False
     return json_menus



def recursion(tmp, depth, json_menus, tmp_menu, depth_check, cyclical_notifier):
     '''
     Function to go through current node ids (tmp) and adds new child id to tmp2 if there are children.

     Goes through cyclical function per id to check if cyclical or not. 

     Checks if no more ids with parent id are left (check length of tmp2), if none left, you've found
     the end of the menu

     Checks depth, if its equal to 4, which is the limit in this challenge, the program will return.
     '''
     if depth == 5:
          return
     tmp2 = []
     for x in tmp:
          try:
               tmp2 += json_menus[x-1]['child_ids']
          except IndexError:
               return
     if len(tmp2) == 0:
          return
     tmp_menu['children'] += tmp2
     cyclical(tmp_menu, cyclical_notifier)
     depth_check.append(tmp2)
     if len(depth_check) == 4:
          return
     depth += 1
     recursion(tmp2, depth, json_menus, tmp_menu, depth_check, cyclical_notifier)

def cyclical(tmp_menu, cyclical_notifier):
     '''
     Check if root ID is in children == cyclical

     Check if there's duplicates in children == cyclical
     '''
     if tmp_menu['root_id'][0] in tmp_menu['children']:
          cyclical_notifier.append(1)
     if len(tmp_menu['children']) != len(set(tmp_menu['children'])):
          cyclical_notifier.append(1)

def place_holder1(json_menus):
     '''
     Creates dictionary to seperate nodes that are parents, and nodes that are children. 
     '''

     place_holder = {'parent': [], 'child': []}
     for x in range(0, len(json_menus)):
          if 'parent_id' in json_menus[x]:
               place_holder['child'].append(json_menus[x]['id'])
          else:
               place_holder['parent'].append(json_menus[x]['id'])
     return place_holder


def json_final1(place_holder, json_menus):
     '''
     Goes through all parent ID's and checks every child node to connect them to it's parent ID.

     Checks c list to see if cyclical or not. Refer to cyclical() function

     Appends menu to final dictionary as either a valid or invalid menu.
     '''
          
     json_final = {'valid menus': [], 'invalid menus': []}
     for x in place_holder['parent']:
          tmp_menu= {'root_id': [x], 'children': []}
          tmp = [x]
          cyclical_notifier = []
          depth_check = []
          recursion(tmp, 1, json_menus, tmp_menu, depth_check, cyclical_notifier)
          if len(cyclical_notifier) > 0:
               json_final['invalid menus'].append(tmp_menu)
          else:
               json_final['valid menus'].append(tmp_menu)
     return json_final
                    
def p_print(data):
     '''
     list OR JSON is printed
     '''
     pp = pprint.PrettyPrinter(indent=4)
     pp.pprint(data)

main()
