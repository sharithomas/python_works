# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 20:30:27 2020

@author: SHARI
"""

#22.	Write a  program to remove last occurrence of a character from string.
str1=input("enter a string:")
ch=input("enter a character ")
#reverse of string
str2=str1[::-1]
#postion of given character from last
position=str2.index(ch)
#calculating last postion of character 
last_position=(len(str1)-position)-1

#removing last occurrence of ch from str1
str3=str1[0:last_position]+str1[last_position+1:]

print("\n  after removing last occurrence of '{}' from {} : {}".format(ch,str1,str3))