# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 10:24:13 2020

@author: SHARI
"""

#29.	Write a  program to find last occurrence of a word in a given string.
str1=input("enter a string:")
str2=input("enter a word to search:")
last_position=str1.rfind(str2)+1
print("\n last occurrence of '{}' in '{}' at '{}' position".format(str2,str1,last_position))