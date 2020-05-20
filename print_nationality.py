# -*- coding: utf-8 -*-
"""
Created on Mon May 18 14:37:28 2020

@author: SHARI
"""

#Define a class named American which has a static method called printNationality.
class American():
    @staticmethod 
    def printNationality(): # static method definition
        print("America")

anAmerican = American()
anAmerican.printNationality()
American.printNationality()