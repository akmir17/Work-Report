# -*- coding: utf-8 -*-
"""
Created on Wed May 11 12:17:57 2022

@author: user
"""


def factorial(n :int) -> int:
    if not isinstance(n, int):
        print('factorial is just for int')
        return None 
    elif n < 0:
        print('factroial is just for adad mosbat')
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)
 