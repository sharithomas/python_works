# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 19:54:52 2020

@author: SHARI
"""

#Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
list_in=[1,2,3,4,5,6,7,8,9,10]
print("given list",list_in)
list_out=list(map(lambda x:x*x,list_in))
print("output  list",list_out)