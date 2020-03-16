# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:28:39 2020

@author: SHARI
"""

#10.	Write a  program to count total number of words in a string.
str1=input("enter a string")
space=0
#count spaces in the string 
for i in str1:
    if i==" ":
        space+=1
#words will be one more than spaces        
words=space+1
print("given string is",str1)
print("total words=",words)