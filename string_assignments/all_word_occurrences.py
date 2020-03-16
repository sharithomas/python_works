# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 10:39:57 2020

@author: SHARI
"""

#30.	Write a program to search all occurrences of a word in given string.
str1=input("enter a string:")
word=input("enter the woord to search:")
position=[i+1 for i in range(len(str1)) if str1.startswith(word,i)]
print("all the occurrences of '{}' in '{}' are {}".format(word,str1,position))
