# -*- coding: utf-8 -*-
"""
Created on Mon May 18 14:57:18 2020

@author: SHARI
"""

#	Please write a program which prints all permutations of [1,2,3]

import itertools
per=input("enter list in comma seperated form ").split(",")  # eg; 1,2,3 then per=[1,2,3]

per=itertools.permutations(per) # permutations using in-built function
for i in list(per):
    print(i)
