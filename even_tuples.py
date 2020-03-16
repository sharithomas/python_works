# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 17:59:39 2020

@author: SHARI
"""

#Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10)
tuple_input=(1,2,3,4,5,6,7,8,9,10)
#even numbers  from the given tuple
tuple_output=(x for x in tuple_input if x%2==0)
print(" all even numbers from the given tuple")
for i in tuple_output:
    print(i,end=",")
