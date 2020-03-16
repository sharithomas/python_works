# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:57:37 2020

@author: SHARI
"""

#15.	Write a  program to find last occurrence of a character in a given string.
str1=input("enter a string:")
ch=input("enter the character to be checked:")
#reverse of string
str2=str1[::-1]
#postion of given character from last
position=str2.index(ch)
#calculating last postion of character 
last_position=len(str1)-position

print("\n last occurrence of '{}' in '{}' at '{}' position".format(ch,str1,last_position))