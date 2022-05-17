# -*- coding: utf-8 -*-
"""
Created on Fri May 13 21:52:07 2022

@author: user
"""

class Shomaresh:
    def __init__ (self, v:int = 0, i:int = 1) -> None:
        self.val = v
        self.incr = i
        
    def afzayesh(self) -> None:
        self.val += self.incr

    def __repr__(self):
        return str(self.val)
        