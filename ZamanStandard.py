# -*- coding: utf-8 -*-
"""
Created on Sun May 15 17:24:34 2022

@author: user
"""


class Zaman:
    def print_zaman(self):
        print('%.2d: %.2d: %.2d' % (self.saat, self.daghighe, self.sanie))
        
    def afzayesh(self, sanieha):
        sanieha += self.zaman_be_int()
        return self.int_be_zaman(sanieha)
    
    def int_be_zaman(self, sanieha):
         daghigheha, self.sanie   = divmod(sanieha, 60)
         self.saat, self.daghighe = divmod(daghigheha, 60)
         return self
    
    def zaman_be_int(self):
        daghigheha = self.saat * 60 + self.daghighe
        sanieha = daghigheha * 60 + self.sanie
        return sanieha 