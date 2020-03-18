# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 13:42:53 2020

@author: SHARI
"""

#Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.
class Rectangle():
    #defintion for init() function
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    #definition for area of rectangle
    def area(self):
        area_rect=self.length*self.breadth
        return area_rect

length=int(input("length"))
breadth=int(input("breadth"))
#constructor
Area=Rectangle(length,breadth)
print("\n Area of a rectangle with length {} and breadth {} is:{} ".format(length,breadth,Area.area()))

