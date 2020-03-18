# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 22:15:49 2020

@author: SHARI
"""

#Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words
# and sorting them alphanumerically. Suppose the following input is supplied to the program: hello world and practice makes perfect and 
#hello world again  Then, the output should be: again and hello makes perfect practice world
print("enter words seperated with white spaces")
list_in=input().split(" ")
list_out=[]
for i in list_in:
    if i not in list_out:
        list_out.append(i)
list_out.sort()
print("result after removing duplicate words and sorting it:\n")
for i in list_out:
    print(i,end=" ")