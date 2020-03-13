# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 11:25:37 2020

@author: SHARI
"""

#Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters. 
#Suppose the following input is supplied to the program: Hello world! 
#Then, the output should be: UPPER CASE 1 LOWER CASE 9
print("enter a sentence")
str1=input()
upper=0
lower=0
#cheking upper case and lower case for each characters
for i in str1:
    if i.islower():
        lower=lower+1
    elif i.isupper():
        upper=upper+1
    else:
        pass
    
print("UPPER CASE :",upper) 
print("LOWER CASE :",lower) 