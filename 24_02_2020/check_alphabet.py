# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:04:17 2020

@author: SHARI
"""

#Write a program to check whether character is an alphabet or not using conditional operator
ch=input("enter a character")
result= "alphabet" if ((ch>='A' and ch<='Z') or (ch>='a' and ch<='z')) else "not an alphabet "
print("{} is ".format(ch),result)
  
    
