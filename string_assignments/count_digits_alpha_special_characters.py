# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:11:48 2020

@author: SHARI
"""

#8.	Write a  program to find total number of alphabets, digits or special character in a string.
str1=input("enter a string")
alphabet=0
digit=0
special_character=0
for i in str1:
    if i.isalpha():
        alphabet+=1
    elif i.isdigit():
        digit+=1
    elif i.isidentifier:
        special_character+=1
    else:
        pass
        
print("given string is",str1)
print("alphabets=",alphabet)
print("digits=",digit)
print("special characters",special_character )

        