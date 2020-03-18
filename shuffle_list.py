# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 12:45:08 2020

@author: SHARI
"""

#Please write a program to shuffle and print the list [3,6,7,8].


from random import shuffle
print("enter list elements in comma seperated form ")
list_in=input().split(",")
print("given list is",list_in)
#shuffle list
shuffle(list_in)
print("shuffled list",list_in)
