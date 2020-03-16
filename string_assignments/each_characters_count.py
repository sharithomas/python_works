# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 13:44:13 2020

@author: SHARI
"""

#20.	Write a  program to count frequency of each character in a string.
str1=input("enter a string:")
characters=[]
#seperate each characters from str1 and add one time to characters list
for i in str1:
    if i not in characters:
        characters.append(i)
for x in characters:
    print("{} in {}=".format(x,str1),str1.count(x))
 