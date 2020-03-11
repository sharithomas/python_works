# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 11:59:06 2020

@author: SHARI
"""
#Define a function that can accept two strings as input and concatenate them and then print it in console.
print("enter 2 strings")
str1=input()
str2=input()
#function for string concatenation
def str_concat(str1,str2):
    return(str1+str2)
    
print("concatenated string is:",str_concat(str1,str2))
