# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 22:46:45 2020

@author: SHARI
"""

#With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], 
#write a program to make a list whose elements are intersection of the above given lists.
list1=[1,3,6,78,35,55]
list2=[12,24,35,24,88,120,155]
print("given lists are")
print("list1",list1)
print("list2",list2)
#function to find intersection of list1 and list2
def intersection(list1,list2):
    list3=[x for x in list1 if x in list2]
    return list3

list3=intersection(list1,list2)
print("intersection of list1 and list2: ")
print(list3)


