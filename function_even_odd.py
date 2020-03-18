# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 12:06:03 2020

@author: SHARI
"""

#Define a function that can accept an integer number as input and print the "It is an even number" 
#if the number is even, otherwise print "It is an odd number".

#function definition to check number is even or odd
def even_fun(number):
    if number%2==0:
        print("{} is even".format(number))
    else:
        print("{} is odd".format(number))
number=int(input("enter number"))
even_fun(number)
        