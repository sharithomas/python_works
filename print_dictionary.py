# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 22:37:04 2020

@author: SHARI
"""

#Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.


#fucntion definition to create and print a dictionary
def dictionary_square():
    dictionary={}
    for i in range(1,4):
        dictionary[i]=i*i
    print(dictionary)
dictionary_square()