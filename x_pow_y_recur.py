# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 07:18:49 2020

@author: SHARI
"""
#Date:05/06/2020
# Write a recursive function to calculate X power Y. X and Y inputs should be read from input. Negative values, zero's need to be checked and error should be thrown in TRY/Except block.
x=int(input("enter value for x"))
y=int(input("enter value for y"))

def power(x,y): # recursive function for x power y
    if y==0:
        return 1
    else: # if y is positive call power() function recursively
        return(x*(power(x,y-1)))

try: #try/except block to catch error occur if y is negative
    result=power(x,y)
    print("{0} power {1}=".format(x,y),result)
except:
    print("Recursion error due to negative value")
    


