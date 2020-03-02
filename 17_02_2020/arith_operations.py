# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 22:17:17 2020

@author: SHARI
"""

#3.	Write a  program to enter two numbers and perform all arithmetic operations.
print("enter two numbers")
a=float(input())
b=float(input())
add= a + b
diff=a - b
div=a / b
rem=a % b
exp=a ** b
mul=a*b
x = a // b
print("a+b=", add)
print("a-b=", diff)
print("a/b=", div)
print("a*b=", mul)
print("a%b=", rem)
print("a//b=", x)
print("a^b=", exp)