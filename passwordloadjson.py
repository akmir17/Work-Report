# -*- coding: utf-8 -*-
"""
Created on Tue May 17 18:05:51 2022

@author: user
"""

import json

esme_file = 'password.json'

try:
    with open(esme_file) as f:
        password = json.load(f)
    
except FileNotFoundError:
    password = input('password ra vared konid: ')
    with open(esme_file, 'w') as f:
        json.dump(password, f)
        print(f'password taeen shode tavasote shoma: {password}')
        
else:
    print(f'password shoma: {password} bood')
    