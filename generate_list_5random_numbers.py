# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 13:51:42 2020

@author: SHARI
"""

#Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive
import random
count=0
list_out=[]
print("\nlist with 5 random numbers between 100 and 200\n")
while count<5:
    #random.randint() used to generate a random integer 
    list_out.append(random.randint(100,201))
    count=count+1
print(list_out)
