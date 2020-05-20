# -*- coding: utf-8 -*-
"""
Created on Mon May 18 11:02:49 2020

@author: SHARI
"""

#A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with
# a given steps. The trace of robot movement is shown as the following: UP 5 DOWN 3 LEFT 3 RIGHT 2 
#if The numbers after the direction are steps. Please write a program to compute the distance from current position after 
#a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
#Example: If the following tuples are given as input to the program: UP 5 DOWN 3 LEFT 3 RIGHT 2 
#Then, the output of the program should be: 2
import math 

x,y=0,0

def distance(x,y): #FUNCTION DEFINITION FOR SQRT(X^2+Y^2)
    return math.sqrt(x**2+y**2)

while True:
    
    point=input("enter movement in UP/DOWN/LEFT/RIGHT format\n") # eg: UP 4 DOWN 2 LEFT 2 RIGHT 4 = (2,2)=SQRT(4+4)
    if point=="":
        break
    else:
        point=point.split() # EG: IF UP 4 GIVEN THEN , point=["UP",4]
        
        if point[0]=="UP":
            y=y+int(point[1])
        elif point[0]=="DOWN":
            y=y-int(point[1])
        elif point[0]=="LEFT":
            x=x-int(point[1])
        else:
            x=x+int(point[1])
    
print("Distance=",distance(x,y))   

    


    