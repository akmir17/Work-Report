# -*- coding: utf-8 -*-
"""
Created on Wed May 11 13:29:09 2022

@author: user
"""

def fibonachi(n :int):
    if n == 0 :
        return(0)
    elif n == 1 :
        return(1)
    else:
        return fibonachi(n-1) + fibonachi(n-2)
    