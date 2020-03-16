# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 13:51:18 2020

@author: SHARI
"""

##18.	Write a  program to find highest frequency  character in a string.
str1=input("enter a string:")
characters=[]
character_dict={}
large=0
#seperate each characters from str1 and add one time to characters list
for i in str1:
    if i not in characters:
        characters.append(i)
#save each character and its count to a dictionary
for x in characters:
    character_dict[x]=str1.count(x)
    
#from dictionary extracting highest frequency item
for x,y in enumerate(character_dict):
    if (character_dict[y]>large):
        large=character_dict[y]
        index=y

print("\n highest frequency character  is '{}', '{}'  times in '{}'".format(index,large,str1))
   
