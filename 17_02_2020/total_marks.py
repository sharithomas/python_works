# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 12:09:37 2020

@author: SHARI
"""

#16.	Write a  program to enter marks of five subjects and calculate total, average and percentage.
print("enter marks of 5 subjects")
print("ener maximum mark of subjects")
m1=float(input())
m2=float(input())
m3=float(input())
m4=float(input())
m5=float(input())
maximum =int(input())
total = m1+m2+m3+m4+m5
avg= total/5
per=(total/(maximum*5))*100
print("total=",total, "\n average=", avg, "\n percentage=",per)