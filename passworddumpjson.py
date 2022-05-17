# -*- coding: utf-8 -*-
"""
Created on Tue May 17 17:49:07 2022

@author: user
"""

import json

password = input('password ra vared konid: ')

esme_file = 'password.json'
with open(esme_file, 'w') as f:
    json.dump(password, f)
    print(f'password taeen shode tavasote shoma {password}')
    