# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 07:50:33 2020

@author: SHARI
"""
#Please write assert statements to verify that every number in the list [2,4,6,8] is even.
n=int(input("enter limit"))
print("enter elements of list")
list_in=[]
for i in range(n):
    list_in.append(input())



for i in list_in:
    assert int(i)%2 ==0, "all elements  are not even "
    print( i + "\t is even")
    
