# -*- coding: utf-8 -*-
"""
Created on Fri May 15 21:13:04 2020

@author: SHARI
"""
#	Define a class which has at least two methods: getString: to get a string from console input printString:
# to print the string in upper case. 
#Also please include simple test function to test the class methods. Hints: Use __init__ method to construct some parameters
class String:
    def __init__(self):
        print("Init function block")
        
    def input_string(self):
        self.str_in=input("enter string")
        
    def print_string(self):
        print("output string:"+self.str_in.upper())
    
string=String()
string.input_string()
string.print_string()

        
