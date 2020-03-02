# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 11:13:32 2020

@author: SHARI
"""

#12.	Write a  program to enter any number and calulate its square root.
import math
n=int(input("enter a number"))
s=math.sqrt(n)
print("square root using math function  ",s)

s1=n**0.5
print("square root using equation number**(1/2) = ",s1)