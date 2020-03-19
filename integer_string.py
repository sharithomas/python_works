# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 14:16:31 2020

@author: SHARI
"""

#Define a function that can convert an integer into a string and print it in console.

#function to convert integer to a string
def integer_string(integer):
    string=str(integer)
    print("integer in string format"+ string)
    

integer=int(input("enter an integer number"))
integer_string(integer)