# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 10:06:53 2020

@author: SHARI
"""

#26.	Write a  program to replace last occurrence of a character with another in a string.
str1=input("enter a string:")
ch1=input("enter character to replace:")
ch2=input("enter  new character ")

#reverse of string
str2=str1[::-1]
#postion of given character from last
position=str2.index(ch1)
#calculating last postion of character 
last_position=len(str1)-position-1

#concatenating all charcters of str1 after replacing ch1 from last  by ch2
str2=str1[:last_position]+ch2+str1[last_position+1:len(str1)]

print("after replacing last occurrence of '{}' by '{}' from string '{}' is '{}'".format(ch1,ch2,str1,str2))
