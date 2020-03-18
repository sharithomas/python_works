# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 14:08:56 2020

@author: SHARI
"""

#Write a program to compute: f(n)=f(n-1)+100 when n>0 and f(0)=1 with a given n input by console (n>0). Example: If the following n is given as input to the program: 5 Then, the output of the program should be: 500.
def f(n):
    if n==0:
        return 0
    else:
        return (f(n-1)+100)
n=int(input("enter value of n"))
result=f(n)
print("result for value {} is {}".format(n,result))

    