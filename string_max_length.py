# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 14:47:59 2020

@author: SHARI
"""

#Define a function that can accept two strings as input and print the string with maximum length in console.
# If two strings have the same length, then the function should print all strings line by line.
def string_fun():
    string1=input("1st string")
    string2=input("2nd string")
    len1=len(string1)
    len2=len(string2)   
    print("\n string with maximum length is")
    if(len1>len2):
        print(string1)
    elif (len2>len1):
        print(string2)
    else:
        print(string1)
        print(string2)
string_fun()