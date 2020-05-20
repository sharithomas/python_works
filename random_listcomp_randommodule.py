# -*- coding: utf-8 -*-
"""
Created on Tue May 19 14:06:15 2020

@author: SHARI
"""

#Please write a program to output a random number, which is divisible by 5 and 7, between 0 and 100
# inclusive using random module and list comprehension.
import random
a=random.choice([x for x in range(101) if x%5==0 and x%7==0]) #  random.choice to select a number randomly from list
print(a)