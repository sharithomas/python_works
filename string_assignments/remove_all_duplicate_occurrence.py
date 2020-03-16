# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 22:10:04 2020

@author: SHARI
"""

#24	Write a program to remove all repeated characters from a given string..
str1=input("enter a string:")
pos=0
character_list=[]
#creating a list with all characters without duplicate
for i in str1:
    if i not in character_list:
        character_list.append(i)
character_dict={}
#dictionary with characters as index and its count as value
for i in character_list:
    character_dict[i]=str1.count(i)

#if count in the character is less than 1 (no duplicate character)print it else wont print
for i in character_dict:
    if character_dict[i]<2:
        print(i,end="")
        
