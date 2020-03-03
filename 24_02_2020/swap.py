# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 07:29:53 2020

@author: SHARI
"""

#Write a program to swap two numbers using bitwise operator
num1=int(input("enter 1st number"))
num2=int(input("enter 2nd number"))
print("before swapping :")
print("number1=",num1,"number2=",num2)

num1=num1^num2 #bitwwise XOR operation
num2=num1^num2
num1=num1^num2
print("after swapping :")
print("number1=",num1,"number2=",num2)

