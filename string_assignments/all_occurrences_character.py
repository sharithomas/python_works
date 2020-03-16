# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 13:35:18 2020

@author: SHARI
"""

#16.	Write a program to search all occurrences of a character in given string.
str1=input("enter a string:")
ch=input("enter the character to be checked:")
print("occurrences of {} in {}:".format(ch,str1))
pos=0
for i in str1:
    pos+=1
    if ch==i:
        print(pos)
