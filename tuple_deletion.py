# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:25:34 2020

@author: SHARI
"""

# Create a tuple (1,2,3,4,5,6), then remove element 5 from it
tuple1=tuple((1,2,3,4,5,6))
print("orginal tuple")
print(tuple1)
list1=list(tuple1)
list1.remove(5)
tuple2=tuple(list1)
print("after removing 5")
print(tuple2)
