# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 15:11:28 2020

@author: SHARI
"""

#The Fibonacci Sequence is computed based on the following formula: f(n)=0 if n=0 f(n)=1 if n=1 f(n)=f(n-1)+f(n-2) if n>1 
#Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.
# Example: If the following n is given as input to the program: 7 Then, the output of the program should be: 13
n=int(input("enter limit"))
fib_list=[]
def fib_fun(n):
    if n==0:
        return 0 
    elif n==1:
        return 1
    else:
        return fib_fun(n-1)+ fib_fun(n-2)
fib_list=fib_fun(n)

