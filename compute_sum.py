# -*- coding: utf-8 -*-
"""
Created on Tue May 19 13:45:26 2020

@author: SHARI
"""

#Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.

def sum_num(a,b):
    return int(a)+int(b)

a=input("enter 1st number")
b=input("enter 2nd number")
print("sum=",sum_num(a,b))