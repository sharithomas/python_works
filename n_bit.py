# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 09:52:43 2020

@author: SHARI
"""

#Write a program to get nth bit of a input number.
binary_num=list()
decimal_num= int(input("enter number"))
n=int(input("enter which bit to be retireve"))

#converting decimal to binary number
for i in range(0,8):
    shift=decimal_num>>i  # code to check value of last bit and append 1 or 0 to list make binary number
    if shift&1:
        binary_num.append(1)
    else:
        binary_num.append(0)
print("\nbinary representation is")
for j in range(-1,-9,-1):
    print(binary_num[j],end="")
#assigining nth bit to a variable n_bit
n_bit=binary_num[n]
print("\n {}th bit of  {} in 8bit representation is {}".format(n,decimal_num,n_bit))