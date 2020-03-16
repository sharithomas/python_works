# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 11:35:33 2020

@author: SHARI
"""

#write a program to find length of a string 
str1=input("enter a string")
len1=len(str1)
len2=0
for i in str1:
    len2=len2+1
print("length of string {} using len() function ".format(str1),len1)
print("\n length of string {} without using len() function ".format(str1),len2)
