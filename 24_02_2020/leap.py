# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 14:47:23 2020

@author: SHARI
"""

##Write a program to check whether year is leap year or not using conditional operator.
year=int(input("enter the year"))   

result="leap year" if ((year%4==0 and year%100==0 and year%400==0) or(year%4==0 and year%100!=0)) else "not leap year"
print("{} is ".format(year),result)
