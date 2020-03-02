# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 08:47:16 2020

@author: SHARI
"""

#10.	Write a  program to convert days into years, weeks and days.
print("enter total days")

d=int(input())
y=d//365#year is calculated

d=d%365 #remaining days after removing above years 
m=int(d/30)

d=d%30#remaining days after removing month days
w=int(d/7)

d=d%7#remaining days
print("year =" ,y)
print("month =" ,m)
print("week =" ,w)
print("days =" ,d)



