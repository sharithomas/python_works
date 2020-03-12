# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 13:13:40 2020

@author: SHARI
"""

#Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console. 
#Example: If the following n is given as input to the program: 10 Then, the output of the program should be: 0,2,4,6,8,10

n=int(input("enter value of n"))
#function to find even numbers using yield
def even_num():
    for i in range(n+1):
        if i%2==0:
            yield i
print("even numbers upto",n)
for i in even_num():
    print(i,end=",")
    
