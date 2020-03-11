# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 10:41:24 2020

@author: SHARI
"""

#find the LCM of any number
input("enter 2 numbers")
a=int(input())
b=int(input())
def Lcm_fun():
    if a>b:
        large=a
    else:
        large=b
    while (1):
        if large%a==0 and large%b==0:
            lcm=large
            break
        large=large+1
    return lcm
print("LCM of {} and {} is {}".format(a,b,Lcm_fun()))
