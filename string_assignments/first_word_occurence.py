# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 10:19:03 2020

@author: SHARI
"""

#28.	Write a  program to find first occurrence of a word in a given string.
str1=input("enter a string:")
str2=input("enter a word to search:")
position = str1.index(str2)
print("\n first occurrence of '{}' in '{}' at '{}' position".format(str2,str1,position+1))