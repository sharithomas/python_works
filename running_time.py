# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 22:06:27 2020

@author: SHARI
"""

#Please write a program to print the running time of execution of "1+1" for 100 times.
import time
def sum_n_numbers(n):
    start_time = time.time()
    s = 0
    for i in range(1,n+1):
        s = 1 + 1
    end_time = time.time()
    return s,end_time-start_time

n = 100
print("\nTime to sum of 1 to ",n," and required time to calculate is :",sum_n_numbers(n))
