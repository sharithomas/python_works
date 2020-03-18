# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 18:33:45 2020

@author: SHARI
"""

#Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
# Example: If the following n is given as input to the program: 5 Then, the output of the program should be: 3.55
n=int(input("enter value of n"))
def series(n):
    f=0
    for i in range(1,n+1):
        f=f+(i/i+1)
    return f
result=series(n)
print("1/2+2/3+3/4+...+n/n+1 for {} = {}".format(n,result))