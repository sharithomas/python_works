# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 10:04:49 2020

@author: SHARI
"""

#Write a program to enter P, T, R and calculate Simple Interest and coumpound interest, also in different functions
import math
p=float(input("enter pricipal amount"))
t=float(input("enter time period in years"))
r=float(input("enter intereset rate"))
#function to calculate compound intereset
def compound_interest(p,r,t):
    fci=p*math.pow((1+r/100),t)
    ci=fci-p
    return ci
#function to calculate simple intereset
def simple_interest(p,r,t):
    si=(p*r*t)/100
    return si

print("Compound interest is",compound_interest(p,r,t))
print("simple interest is ",simple_interest(p,r,t))