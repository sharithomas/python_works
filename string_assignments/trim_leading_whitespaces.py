# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 11:17:18 2020

@author: SHARI
"""

#35.	Write a  program to trim leading white space characters from given string
str1=input("enter a string")
#removing leading white spaces
str2=str1.lstrip()
print("'{}' after removing leading white spaces '{}'".format(str1,str2))