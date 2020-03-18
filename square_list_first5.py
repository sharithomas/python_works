# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 07:42:23 2020

@author: SHARI
"""
#Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
#Then the function needs to print the first 5 elements in the list.
n=int(input("enter limit"))
square_list=[]

def square_fun():
    for x in range(1,n+1):
        square_list.append(x*x)
    print(square_list[:5])
    
print("last 5 elemnts from the square list",square_fun())