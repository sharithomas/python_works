# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 08:21:17 2020

@author: SHARI
"""

#Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.
import random
count=0
list_out=[]
while count<5:
    num=random.randint(100,200)
    if num%2==0:
        list_out.append(num)
    else:
        list_out.append(num+1)
    count=count+1
