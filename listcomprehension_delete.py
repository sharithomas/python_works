# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 11:19:18 2020

@author: SHARI
"""

#By using list comprehension, please write a program to print the list after removing delete numbers which are divisible by 5 and 7 
#in [12,24,35,70,88,120,155]. Hints: Use list comprehension to delete a bunch of element from a list.
n=int(input("enter limit"))
list_in=[]
print("enter list elements")
#create list by inputting elements from console
for i in range(n):
    list_in.append(input())
#list out by deleting numbers which are divisible by 5 and 7 from list_in
list_out=[x for x in list_in if int(x)%5!=0 or int(x)%7!=0 ]
print("list after removing numbers which are divisible by 5 and 7:")
print(list_out)