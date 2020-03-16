# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 14:09:52 2020

@author: SHARI
"""

#23.	Write a  program to remove all occurrences of a character from string.
str1=input("enter a string:")
ch=input("enter the character ")     
# Removing all ch from str1 and using join() + list comprehension 
new_str = ''.join([str1[i] for i in range(len(str1)) if str1[i ]!= ch])
print("after removing all the occurrence of '{}' form '{}' is : '{}' ".format(ch,str1,new_str))

