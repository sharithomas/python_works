# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 09:15:11 2020

@author: SHARI
"""

#Please write a program which accepts a string from console and print the characters that have even indexes.
string=input("enter string")
print("given string:",string)
index=0
print("characters with even indexes: ")
for i in string:
    if index%2==0:
        print(string[index],end="")
    index=index+1
