# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 22:18:24 2020

@author: SHARI
"""

#Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
numbers=[1,2,3,4,5,6,7,8,9,10]
print("given list is",numbers)
#create even numbers using filter() function 
even=list(filter(lambda x: x%2==0,numbers ))
#find square of even numbers using map() function 
square_even=list(map(lambda x:x*x,even))
print(square_even)