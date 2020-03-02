# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 10:55:45 2020

@author: SHARI
"""

#11.	Write a  program to find power of any number x ^ y.
print("enter x and y ")
x=int(input())
y=int(input())
z=x
for y in range(1,y,1):
    x=z*x
    
print("x^y =", x)