# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 14:01:08 2020

@author: SHARI
"""

#Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.
import random
count=0
list_out=[]
print("\nlist with 5 random numbers between 1 and 1000 which are divisible by 5 and 7\n")
for x in range(1,1001):
    #random.randint() to generate random integer
    i=random.randint(1,1001)
    #check for divisibility of number by 5 and 7
    if i%5==0 and i%7==0:
        #break from loop list created with 5 numbers
        if count<5:
            list_out.append(i)
            count=count+1
        else:
            break
    
print(list_out)