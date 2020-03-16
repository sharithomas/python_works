# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:20:24 2020

@author: SHARI
"""

#9.	Write a  program to count total number of vowels and consonants in a string.
str1=input("enter a string")
vowel=0
consonant=0
vowel_list=['a','e','i','o','u','A','E','I','O','U']
for i in str1:
    if i in vowel_list:
        vowel+=1
    else:
        consonant+=1
print("given string",str1)
print("vowels=",vowel)
print("consonants=",consonant)