# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 15:32:34 2020

@author: SHARI
"""

#Write a program to set nth bit of a number.
count_zero=0
binary_num=list()
decimal_num= int(input("enter number"))
position=int(input("position to be set"))

# function to convert decimal to binary
def decimal_binary(decimal_num):
    for i in range(0,8):
        shift=decimal_num>>i  # code to check value of last bit and append 1 or 0 to list make binary number
        if shift&1:
            binary_num.append(1)
        else:
            binary_num.append(0)
    return binary_num.reverse()

decimal_binary(decimal_num) # function call
for j in range(0,8):
       print(binary_num[j],end="")
if binary_num[position-1]==0:
    binary_num[position-1]=1

print("\n after set  {} th bit\n".format(position))

for j in range(0,8):
       print(binary_num[j],end="")