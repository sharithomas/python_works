# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 12:27:00 2020

@author: SHARI
"""

#Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".
string_in=input("enter string")
yes_string=['yes','YES','Yes']
if string_in in yes_string:
    print("Yes")
else:
    print("No")