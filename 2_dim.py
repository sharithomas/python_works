# -*- coding: utf-8 -*-
"""
Created on Mon May 18 18:31:13 2020

@author: SHARI
"""

#Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row
# and j-th column of the array should be i*j. Note: i=0,1.., X-1; j=0,1,¡­Y-1. Example Suppose the following inputs are given
#to the program: 3,5 Then, the output of the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
row=int(input("enter number of rows"))
col=int(input("enter number of columns"))
multi_list = [[0 for i in range(col)] for j in range(row)] # create&initilize a multilist with zeros with given rows&columns

for i in range(0,row):
    for j in range(0,col):
        multi_list[i][j]=i*j # save i*j product at each index
    
print(multi_list)