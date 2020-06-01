# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 10:30:58 2020

@author: SHARI
"""
#Please raise a RuntimeError exception. Hints: Use raise() to raise an exception.

x=int(input("enter a number"))
if x<0:
    raise Exception("given number is negative")
elif x==0:
    print("given number is zero")
else:
    print("given number is positive")