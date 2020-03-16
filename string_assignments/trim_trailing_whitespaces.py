# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 11:21:01 2020

@author: SHARI
"""

#36.	Write a  program to trim trailing white space characters from given string.
str1=input("enter a string")
#removing trailing white spaces
str2=str1.rstrip()
print("'{}' after removing trailing white spaces '{}'".format(str1,str2))