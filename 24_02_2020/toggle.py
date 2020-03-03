# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 21:12:00 2020

@author: SHARI
"""

#Write a program to toggle nth bit of a number



num=int(input(" number")) 
n =int(input("position of bit to toggle")) 
print("result after toggling")  
print(num ^ (1 << (n - 1))) # xor with the position bit to toggle

