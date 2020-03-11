# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 11:21:10 2020

@author: SHARI
"""

#Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.
print("enter a sequence of words")
words=input().split(" ")
print("given words are")
print(words)
print("words with only are digits  :")
for x in words:
  if x.isdigit():
      print(x)    
