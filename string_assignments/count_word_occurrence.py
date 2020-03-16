# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 10:54:50 2020

@author: SHARI
"""

#31.	Write a program to count occurrences of a word in a given string

str1=input("enter a string:")
word=input("enter the woord to search:")
#indexes of word in str1
position=[i+1 for i in range(len(str1)) if str1.startswith(word,i)]
count=len(position)
print("total number of occurrences of '{}' in '{}' is '{}' ".format(word,str1,count))