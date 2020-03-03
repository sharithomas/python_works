# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 12:51:47 2020

@author: SHARI
"""

#Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input 
#and then check whether they are divisible by 5 or not.


items = []
num = [x for x in input().split(',')]
for p in num:
    x = int(p, 2)
    if not x%5:
        items.append(p)
print(','.join(items))