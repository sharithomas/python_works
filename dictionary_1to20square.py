# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 07:05:04 2020

@author: SHARI
"""

#Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) 
#and the values are square of keys.The function should just print the values only.
dictionary={}
def dictionary_fun():
    for i in range(1,21):
        dictionary[i]=i*i
        print(dictionary[i],end=",")
    
print("\n values of dictionary are:\n ")
dictionary_fun()
        