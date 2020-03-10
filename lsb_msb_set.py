# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 20:51:19 2020

@author: SHARI
"""

#Write a program to check Least Signifiant Bit (LSB) of a number is set or not and MSB of a number is set or not?

binary_num=list()
decimal_num= int(input("enter number"))

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
lsb=binary_num[7] #LSB value
msb=binary_num[0] #MSB value

#function check for MSB and LSB set
def lsb_msb_check():
    if lsb==1:
        print("\nLSB is set")
    else:
        print("\nLSB not set")
    if msb==1:
        print("\nMSB is set")
    else:
        print("\nMSB not set")
lsb_msb_check()


    
