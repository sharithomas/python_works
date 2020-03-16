# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:52:30 2020

@author: SHARI
"""

#14.	Write a  program to find first occurrence of a character in a given string.
str1=input("enter a string:")
ch=input("enter the character to be checked:")
position=str1.index(ch)
print("\n 1st occurrence of {} in {} at '{}' position".format(ch,str1,position+1))