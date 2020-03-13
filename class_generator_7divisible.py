# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 11:00:18 2020

@author: SHARI
"""
#Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
# Hints: Consider use yield
class Generator():
    def __init__(self,n):
        self.n=n
    def divisible(self):
        for x in range(self.n+1):
            if x%7==0:
                yield(x)
        
        
        
        
print("enter value of n")
n=int(input())
g=Generator(n)
for i in g.divisible():
    print(i)