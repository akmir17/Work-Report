# -*- coding: utf-8 -*-
"""
Created on Wed May 11 13:29:09 2022

@author: user
"""

def fibonacci(n :int):
    if n == 0 :
        return(0)
    elif n == 1 :
        return(1)
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    