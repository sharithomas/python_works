# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 14:21:30 2020

@author: SHARI
"""

#21.	Write a  program to remove first occurrence of a character from string
str1=input("enter a string:")
ch=input("enter a character")
position=0
for i in str1:
    position+=1
    if i==ch:
        break
    else:
        pass

str2=str1[0:position-1]+str1[position:]
print("\n after removing 1st occurrence of '{}' from {} : {}".format(ch,str1,str2))


        
        