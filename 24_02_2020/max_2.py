# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 07:26:49 2020

@author: SHARI
"""

#Write a program to find maximum between two numbers with/without using conditional operator.
num1=input("1st number")
num2=input("2nd number")
large= num1 if num1>num2 else num2
print("largest number =",num1)