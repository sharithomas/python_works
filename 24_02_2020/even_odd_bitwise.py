# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 08:33:55 2020

@author: SHARI
"""

#Write a program to check whether a number is even or odd using bitwise operator.
number=int(input("enter a number"))
#bitwise AND with 1 give true if it odd else false for even number
if number&1:
    print("{} is an odd number".format(number))
else:
     print("{} is an even number".format(number))
    