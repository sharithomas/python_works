# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 20:56:43 2020

@author: SHARI
"""

#Write a program to get highest set bit of a number.
number=int(input("enter number"))

# function to find msb bit, ie for 18 output is 16
def largebit_set(number):
    if number==0:
        return 0
    msb=0
    while(number>0):
        number=int(number/2)
        msb+=1
    return(1<<msb-1)
print(largebit_set(number))


