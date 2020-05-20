# -*- coding: utf-8 -*-
"""
Created on Mon May 18 22:29:47 2020

@author: SHARI
"""

#Define a class named American and its subclass NewYorker.
class American:
    def __init__(self,name):
        self.nation=name
        
    def Nationality(self):
        print(self.nation)
        
class Newyorker(American):
    def Nationality(self):
        print(self.nation)
        
anAmerican=American("American")
anAmerican.Nationality()

aNewyorker=Newyorker("NewYorker")
aNewyorker.Nationality()



