# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 11:01:35 2020

@author: SHARI
"""

#32.	Write a  program to remove first occurrence of a word from string.
str1=input("enter a string:")
word=input("enter a word to remove")
#index of first occrrence of word in str1
position=str1.index(word)
length=len(word)
#removing 1st occurrence of word from str1
str2=str1[:position]+str1[position+length:]

print("\n after removing 1st occurrence of '{}' from '{}' : '{}' ".format(word,str1,str2))


        