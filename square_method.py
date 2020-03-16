# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 18:35:05 2020

@author: SHARI
"""

#Write a method which can calculate square value of number
class Square():
    def __init__(self,number):
        self.number=number
    def square_number(self):
        return(self.number*self.number)
n=int(input("enter a number"))
square=Square(n)
print("square of {} is {}".format(n,square.square_number()))