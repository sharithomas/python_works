# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:37:35 2020

@author: SHARI
"""

#12.	Write a  program to check whether a string is palindrome or not.
str1=input("enter a string")
#function to find reverse of string
def string_reverse(str1):
    reverse_string=str1[::-1]
    return reverse_string
    
reverse=string_reverse(str1)

#if string and reverse of it are equal then its a palindrome else not
if reverse==str1:
    print("{} is palindome string".format(str1))
else:
    print("{} is not  palindome string".format(str1))
    
