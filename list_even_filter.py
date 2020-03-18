# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 12:52:58 2020

@author: SHARI
"""

#Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).
print("even numbers between 1 and 20")
result=list(filter(lambda x:x%2==0,range(1,21)))
print(result)