# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 14:08:20 2020

@author: SHARI
"""

##19.	Write a  program to find lowest frequency  character in a string.
str1=input("enter a string:")
character_dict={}  
#save count of each character in a dictionary 
for i in str1: 
    if i in character_dict: 
        character_dict[i] += 1
    else: 
        character_dict[i] = 1
#check for smallest count charcter in str1
small=1
for x,y in enumerate(character_dict):
    if (character_dict[y]<=small):
        small=character_dict[y]
        index=y
print("\n lowest frequency character  is '{}', '{}'  times in '{}'".format(index,small,str1))
    
    
