# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 21:39:33 2020

@author: SHARI
"""

#Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).

square_number=list(map(lambda x:x*x,list(range(1,21))))
print("list with square of numbers between 1 and 20")
for i in square_number:
    print(i,end=",")