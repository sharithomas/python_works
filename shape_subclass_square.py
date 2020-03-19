# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 07:56:44 2020

@author: SHARI
"""

#Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument.
# Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

#class named shape and defined its area function
class Shape():
    def area(self):
        return 0
#class square and it contain init() and area functions    
class Square(Shape):
    def __init__(self,length):
        self.length=length
    def area(self):
        return self.length*self.length
    
print("enter the length of the square")
length=int(input())
square=Square(length)
square.area()