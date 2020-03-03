# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 07:11:13 2020

@author: SHARI
"""

#Write a program to compute the frequency of the words from the input.
words=input(" input string")
find=input("enter substring")
count=words.count(find)
print("frequency of {} in the string {} is {}".format(find,words,count))