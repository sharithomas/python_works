# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:40:30 2020

@author: SHARI
"""

#Create a list and remove last element from it.
list1=list([1,2,3,4,5,6])
print("orginal list is ")
print(list1)
list1.remove(len(list1)) # remove last element
print("list after removing last element")
print(list1)