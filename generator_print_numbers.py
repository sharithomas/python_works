# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 10:00:05 2020

@author: SHARI
"""

# write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while
# n is input by console. Example: If the following n is given as input to the program: 100 Then, the output of the program should be: 0,35,70


n=int(input("enter value of n"))
#generator function to print numbers which are divisible by 5 and 7 with in range of n
def function(n):
    for i in range(n):
        if i%5==0 and i%7==0:
            yield i

for i in function(n):
    print(i,end=",")