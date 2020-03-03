# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 14:32:32 2020

@author: SHARI
"""

#Write a program to find maximum between three numbers using conditional operator
a=input("enter 1st number")
b=input("enter 2nd number")
c=input("enter 3rd number")
big= a if a>b else b
biggest= big if big>c else c
print("largest number is",big)