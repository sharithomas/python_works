# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 22:10:33 2020

@author: SHARI
"""

#Write a program that accepts a sentence and calculate the number of letters and digits. 
#Suppose the following input is supplied to the program: hello world! 123 Then, the output should be: LETTERS 10 DIGITS 3
string=input("enter string")
letter=0
digit=0
for i in  string:
    if i.isdigit():
        digit=digit+1
    elif i.isalpha():
        letter=letter+1
    else:
        pass
print("letters : {} and digits :{}".format(letter,digit))
    
    