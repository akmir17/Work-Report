# -*- coding: utf-8 -*-
"""
Created on Thu May 12 11:08:24 2022

@author: user
"""


def func1(*args):
    for arg in args :
        print(arg)
        

def func2(**kwargs):
    for k, v in kwargs.items():
        print('%s : %s' %(k,v))
        
        
def func3(arg1, arg2, arg3):
    print('arg1', arg1)
    print('arg2', arg2)
    print('arg3', arg3)
    
    
def miangin(aval, *baghi):
    return(aval + sum(baghi)) / (1 + len(baghi))
