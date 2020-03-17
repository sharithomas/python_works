# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 09:06:45 2020

@author: SHARI
"""

#Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].
list_input=[5,6,77,45,22,12,24]
print("\ngiven list is")
for i in list_input:
    print(i,end=",")
list_out=[x for x in list_input if x%2!=0]
print("\n after removing even numbers from given list :")
for i in list_out:
    print(i,end=",")