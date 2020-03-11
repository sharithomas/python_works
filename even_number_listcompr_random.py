# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 10:38:44 2020

@author: SHARI
"""

#Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.
import random 
print("enter range value")
n=int(input())
#list comprehension to create a list of  even numbers in the given range
x=[x  for x in random.range(0,n) if x%2==0]

#random choice() is used to select a number from a given container
print(random.choice(x))
      