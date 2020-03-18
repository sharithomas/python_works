# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 10:54:21 2020

@author: SHARI
"""

#Write a program which can compute the factorial of a given numbers. 
#The results should be printed in a comma-separated sequence on a single line. 
#Suppose the following input is supplied to the program: 8 Then, the output should be: 40320
n=int(input("enter a number"))
#function definition to calculate factorial of n
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=i*fact
    return fact
print("factorial of {} is:".format(n), factorial(n))