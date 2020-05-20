# -*- coding: utf-8 -*-
"""
Created on Fri May 15 21:29:59 2020

@author: SHARI
"""
#Write a program to solve a classic ancient Chinese puzzle:We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
#How many rabbits and how many chickens do we have? Hint: Use for loop to iterate all possible solutions.

#function definition to solve puzzle
def puzzle(numheads,numlegs):
    for rabbit in range(numheads+1):
        chicken=numheads-rabbit
        if 4*rabbit+2*chicken==numlegs:  # no.of rabbit(4legs)+no.of chicken(2legs)= total legs 
    return "invalid input"
    
    
numheads=int(input("enter number of heads"))
numlegs=int(input("enter number of legs"))
solution=puzzle(numheads,numlegs)
print("%d rabbit and %d chickens" %solution)