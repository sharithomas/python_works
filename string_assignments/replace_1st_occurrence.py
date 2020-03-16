# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 08:56:54 2020

@author: SHARI
"""

#25.	Write a  program to replace first occurrence of a character with another in a string.
str1=input("enter a string:")
ch1=input("enter character to replace:")
ch2=input("enter  new character ")
#position of ch1 in the str1
position=str1.index(ch1)

#concatenating all charcters of str1 after replacing ch1 by ch2
str2=str1[:position]+ch2+str1[position+1:len(str1)]

print("after replacing 1st occurrence of '{}' by '{}' from string '{}' is '{}'".format(ch1,ch2,str1,str2))
