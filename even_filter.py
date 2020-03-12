# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 00:00:37 2020

@author: SHARI
"""

#Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].
list1=[1,2,3,4,5,6,7,8,9,10]
print("given list is",list1)
list2=list(filter(lambda x: x%2==0,list1))
print("list with even values")
print(list2)