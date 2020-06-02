# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 15:47:32 2020

@author: SHARI
"""

#Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.

print("enter string")
s =input()
u = s.encode("utf-8") #encoding string in utf-8 code
print(u)