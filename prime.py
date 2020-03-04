# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 18:28:52 2020

@author: SHARI
"""

#given number is prime or not
p=int(input("enter a number"))
flag=0
for i in range(2,p):
    if p%i==0:
        flag=1
        break;
    else:
        pass
if flag==1:
    print("{} is not a prime ".format(p))
else:
    print("{} is  a prime ".format(p))