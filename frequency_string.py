# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 07:11:13 2020

@author: SHARI
"""

#Write a program to compute the frequency of the words from the input.

string=input(" input string")

#function to find frequency of each word in a string
def words_frequency(string):
    str1=[]
    string=string.split()
    for i in string:
        if i  not in str1:
            str1.append(i)
#count frequency of each word str1  presentin string
    for i in range(0,len(str1)):
        print("frequency of",str1[i],'is' ,string.count(str1[i]))
  
words_frequency(string)
