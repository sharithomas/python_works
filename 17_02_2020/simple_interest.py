# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 12:21:58 2020

@author: SHARI
"""

#17.	Write a  program to enter P, T, R and calculate Simple Interest.
p=float(input("enter pricipal amount"))
t=float(input("enter time period in years"))
r=float(input("enter interset rate"))
si=(p*r*t)/100
print("simple interest \t " , si)