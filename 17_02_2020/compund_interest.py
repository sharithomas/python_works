# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 13:52:18 2020

@author: SHARI
"""

#18.	Write a  program to enter P, T, R and calculate compound Interest.
import math
p=float(input("enter pricipal amount"))
t=float(input("enter time period in years"))
r=float(input("enter interset rate"))
fci=p*math.pow((1+r/100),t)
ci=fci-p
print("compound interest \t " , ci)