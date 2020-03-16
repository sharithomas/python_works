# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 13:40:57 2020

@author: SHARI
"""

#17.	Write a  program to count occurrences of a character in given string.
str1=input("enter a string:")
ch=input("enter the character to be checked:")
count=0
for i in str1:
    if ch==i:
        count+=1
print("occurences of {} in {} is {} times".format(ch,str1,count))
