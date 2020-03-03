# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 13:39:15 2020

@author: SHARI
"""

#Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) 
#and the values are square of keys.The function should print all key/value combinations.

    
dict1=dict()
# fuction to create and print values , keys of dictionary
def dictionary(a):
    dict1[a]=a*a
    print(a, dict1[a]) 

for x in range(1,21):
    dictionary(x)

