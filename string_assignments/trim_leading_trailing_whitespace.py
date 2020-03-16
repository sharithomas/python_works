# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 11:22:13 2020

@author: SHARI
"""

#37.	Write a  program to trim both leading and trailing white space characters from given string.
str1=input("enter a string")
#removing leading&trailing white spaces
str2=str1.strip()
print("'{}' after removing trailing and leading white spaces '{}'".format(str1,str2))