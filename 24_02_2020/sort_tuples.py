# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 11:21:29 2020

@author: SHARI
"""

#You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers.
n=int(input("enter the limit"))
list1=list()

for i in range(0,n): # accept details from user as tuple and save it in a list
    print("enter details for {} person ",i+1)
    name =input("enter name")
    age=int(input("enter age"))
    score=int(input("enter score"))
    t1=(name,age,score)
    list1.append(t1)

print("given list is ")
print(list1)

list1.sort()
print("after sorting list is ")
print(list1)
    
