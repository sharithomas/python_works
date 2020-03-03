# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 07:44:34 2020

@author: SHARI
"""

#Write a program to check whether a number is even or odd using conditional operator.
number=int(input("enter number"))
result="even" if number%2==0 else "odd" #using conditional operator
print("{} is ".format(number),result)