# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 11:14:08 2020

@author: SHARI
"""

#34.	Write a program to remove all occurrence of a word in given string.
str1=input("enter a string:")
word=input("enter a word to remove")

#replacing word with empty 
print("\n after removing all the  occurrence of '{}' from '{}' : '{}' ".format(word,str1,str1.replace(word,"")))