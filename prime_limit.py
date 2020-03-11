# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 10:19:39 2020

@author: SHARI
"""

#print all the prime numbers between input1(say 100) and input2(say 200)
limit1=int(input("enter 1st limit"))
limit2=int(input("enter 2nd limit"))
def prime_number(limit1,limit2):
    for i in range(limit1,limit2+1):
        flag=0
        for j in range(2,i):
            if i%j==0:
                flag=1
                break;
        if flag==0:
                yield i

for i in prime_number(limit1,limit2):
    print(i)