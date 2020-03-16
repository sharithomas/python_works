# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 11:24:10 2020

@author: SHARI
"""

#38.	Write a  program to remove all extra blank spaces from given string.
str1=input("enter a string")
#removing all extra blank spaces
str2=str1.replace(" ","")
print("'{}' after removing trailing and leading white spaces '{}'".format(str1,str2))