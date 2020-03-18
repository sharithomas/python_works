# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 07:16:50 2020

@author: SHARI
"""

n=int(input("enter limit"))
#function for fibannocci series
def fib(n):
    a=0
    b=1
    for i in range(n):
        print(a,end=",")
        a,b=b,a+b
fib(n)