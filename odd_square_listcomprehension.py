# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 13:57:17 2020

@author: SHARI
"""

#Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. 
#Suppose the following input is supplied to the program: 1,2,3,4,5,6,7,8,9 Then, the output should be: 1,3,5,7,9

values=input("enter numbers")
list_value=values.split(",")
#seperating each odd numbers from list and find its sqaure and assign to a list
result=[int(x)*int(x) for x in list_value if int(x)%2!=0 ]
print("\n square of odd numbers from list is ")
for i in result:
    print(i,end=",")

    
