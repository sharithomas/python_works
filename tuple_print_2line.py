# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 10:43:31 2020

@author: SHARI
"""

#With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.
tuple1=(1,2,3,4,5,6,7,8,9,10)
count=0
for i in range(0,len(tuple1)//2):
    if i==6:
        break;
    else:
        print(tuple1[i],end=" ")
        count=count+1
print("\n")
for i in  range(count,len(tuple1)):
    print(tuple1[i],end=" ")

    
    
    
        
    