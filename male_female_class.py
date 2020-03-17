# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 07:35:51 2020

@author: SHARI
"""

#Define a class Person and its two child classes: Male and Female. 
#All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class
class Person():
    def __init__(self,name):
        self.name=name
        
class Male(Person):
    def getGender(self):
        return(self.name+': male')
        
    
class Female(Person):
    def getGender(self):
        return(self.name+': female')

male=Male("Ram")
female=Female("Rani")
print(male.getGender())
print(female.getGender())
        