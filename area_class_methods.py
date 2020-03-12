# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 23:31:40 2020

@author: SHARI
"""

#Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.

#class with 2 methods _init_  and area_fun
class Circle():
    def __init__(self,radius):
        self.radius=radius
    def area_fun(self):
        area=3.14*self.radius*self.radius
        return area
print("enter radius of circle")
r=int(input())
circle=Circle(1)
print("area of circle",circle.area_fun())
