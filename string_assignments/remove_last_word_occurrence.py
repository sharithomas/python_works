# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 11:10:25 2020

@author: SHARI
"""

#33.	Write a  program to remove last occurrence of a word in given string.
str1=input("enter a string:")
word=input("enter a word to remove")
#index of last occrrence of word in str1
position=str1.rindex(word)
length=len(word)
#removing last occurrence of word from str1
str2=str1[:position]+str1[position+length:]

print("\n after removing last occurrence of '{}' from '{}' : '{}' ".format(word,str1,str2))


        