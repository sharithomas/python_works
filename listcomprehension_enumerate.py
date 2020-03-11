# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 14:36:59 2020

@author: SHARI
"""

#By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155]. 
#Hints: Use list comprehension to delete a bunch of element from a list. Use enumerate() to get (index, value) tuple.
list1=[12,24,35,70,88,120,155]
print("given list is:\n",list1)
print("\n \nafter deleting 0th,4h and 5th element")
result=[y  for x,y in enumerate(list1) if (x!=0 and x!=4 and x!=5)]
print(result)