# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 07:13:29 2020

@author: SHARI
"""

#Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence
# after sorting them alphabetically. Suppose the following input is supplied to the program: without,hello,bag,world 
#Then, the output should be: bag,hello,without,world 
#Hints: In case of input data being supplied to the question, it should be assumed to be a console input
print("enter words in comma seperated form")
string=input().split(",")
string.sort()
print("\noutput after sorting strings\n")
for i in string:
    print(i,end=",")