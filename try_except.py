# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 13:02:53 2020

@author: SHARI
"""

#Write a function to compute 5/0 and use try/except to catch the exceptions.

#function for try/except
def divide_zero():
    try:
        result=5/0
    except:
        print("zero division error")
    else:
        print("result of zero division is",result)
    

divide_zero()