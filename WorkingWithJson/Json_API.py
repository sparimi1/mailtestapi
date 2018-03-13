'''
Created on Mar 11, 2018
https://maps.googleapis.com/maps/api/geocode/json?address=95310
@author: Administrator
'''

import urllib.parse
import requests

main_api = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Address:')
    if address == 'quit' or address == 'q':
     break 
 
    url = main_api + urllib.parse.urlencode({'address':address})
    
    print(url)
    
    json_data = requests.get(url).json()
    
    json_status = json_data['status']
    
    print('API Status: ' + json_status)
    
    if json_status == 'OK':
        print()
        
        for each in json_data['results'][0]['address_components']:
            
            longname = each['long_name']
            print(longname)
            
        formatted_address  =  json_data['results'][0]['formatted_address']
        
        print()
        
        print(formatted_address)
    else:
     print('please enter valid address code')
