# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 10:15:21 2020

@author: SHARI
"""

#27.	Write a program to replace all occurrences of a character with another in a string.
str1=input("enter a string:")
ch1=input("enter character to replace:")
ch2=input("enter  new character ")
#replacing all ch1 by ch2 from str1
str2=str1.replace(ch1,ch2)

print("after replacing all the occurrence of '{}' by '{}' from string '{}' is '{}'".format(ch1,ch2,str1,str2))