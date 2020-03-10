# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 18:25:47 2020

@author: SHARI
"""
#write a program to find the GCD or HCF of any number

a=int(input("first number"))
b=int(input("second number"))
#function to find gcd of 2 numbers
def gcd_number(a,b):
    small=0
    #find smallest among 2 numbers
    if a<b:
        small=a
    else:
        small=b
     #find largest divisible number from 1 to smallest among a and b   
    for i in range(1,small+1):
        if (a%i==0 and b%i==0):
            gcd=i
    return gcd

gcd_result=gcd_number(a,b)
print("gcd of {} and {} is {}".format(a,b,gcd_result))

