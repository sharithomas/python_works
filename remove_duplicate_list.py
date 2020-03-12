# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 23:50:58 2020

@author: SHARI
"""

#With a given list [12,24,35,24,88,120,155,88,120,155],
# write a program to print this list after removing all duplicate values with original order reserved.
list1=[12,24,35,24,88,120,155,88,120,155]
print("given list",list1)

#sdding elements from  list1 to list2 without duplicate values 
list2=[]
for x in list1:
    if x not in list2:
        list2.append(x)
        
print("list after removing duplicate values",list2)