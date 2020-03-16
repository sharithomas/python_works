# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:41:39 2020

@author: SHARI
"""

#13.	Write a  program to reverse order of words in a given string.
print("enter a string")
# saving each words of string in a list
words=input().split(" ")
print("\n words of string in reverse order:")
#printing words in reverse order
for i in words[::-1]:
    print(i,end=" ")
