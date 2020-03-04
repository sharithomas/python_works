# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 12:04:16 2020

@author: SHARI
"""
# prime number upto a limit

n=int(input("enter limit "))
number=1
while(number<=n):
    count=0
    i=2
    while(i<=number//2):
        if(number%i==0):
            count=count+1
            break 
        i=i+1
    if(count==0 and number!=1):
        print(number)
    number=number+1