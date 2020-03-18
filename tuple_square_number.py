# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 09:24:50 2020

@author: SHARI
"""

#Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).
list_in=[]
#function to generate and print tuples
def tuple_fun():
    for i in range(1,21):
        list_in.append(i*i)
    tuple_in=tuple(list_in)
    for i in tuple_in:
        print(i,end=",")
tuple_fun()