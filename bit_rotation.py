# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 07:33:20 2020

@author: SHARI
"""

#Write a program to rotate bits of a given number.


INT_BITS = 32

#function to rotate left nby d bits
def leftRotate(n, d): 
	return (n << d)|(n >> (INT_BITS - d)) 

#function to rotate right by d bits
def rightRotate(n, d): 
	return (n >> d)|(n << (INT_BITS - d)) & 0xFFFFFFFF


n = int(input("enter number"))
d = int(input("enter no.of postions to shift"))

print("Left Rotation of",n,"by"
	,d,"is",end=" ") 
print(leftRotate(n, d)) 

print("Right Rotation of",n,"by"
	,d,"is",end=" ") 
print(rightRotate(n, d)) 


