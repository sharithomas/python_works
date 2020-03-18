# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 11:01:15 2020

@author: SHARI
"""

#Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program: 34,67,55,33,12,98 Then, the output should be: ['34', '67', '55', '33', '12', '98'] 
#('34', '67', '55', '33', '12', '98')
#creating list
list_in=input("enter list").split(",")
#create tuple by converting list to tuple
tuple_in=tuple(list_in)
print("\n given list and tuples are:")
print(list_in)
print(tuple_in)