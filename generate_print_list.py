# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 13:12:07 2020

@author: SHARI
"""

#Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).
list_square=[]
def square_numbers():
    for i in range(1,21):
        list_square.append(i*i)
    print(list_square)

print("\nlist with square of numbers from 1 to 20:")
square_numbers()