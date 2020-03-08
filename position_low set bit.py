# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 07:20:00 2020

@author: SHARI
"""


# Python Code for Position 
# of rightmost set bit 
  
import math 
  
def getFirstSetBitPos(n): 
  
     return math.log2(n&-n)+1 # take 2's complement of n , then do & with n , take log to find position and ADD 1 
  
  
n = 18
print(int(getFirstSetBitPos(n))) 
  
type(n)