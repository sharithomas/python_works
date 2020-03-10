# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 15:13:51 2020

@author: SHARI
"""

#write a program to find the 2nd most frequently occurring number in a given list. Read list from input
n=int(input("enter no. of elements"))
list1=list()
dict1=dict()
list2=list()
#accept list elements from user
for i in range(n):
    list1.append(input())
    
#function to count frequency of each elements   
def count_number():
    count=0
    for i in list1:
        if i not in dict1:
            count=list1.count(i)
            dict1[i]=count
    return dict1
#call function count_number
count_number()

#create a list and append it with values of dictionary(frequency of numbers)
for i in dict1:
    list2.append(dict1[i])
list2.sort() # sort frequncyof numbers
value=list2[len(list2)-2] # access 2nd frequent item
#printing 2nd frequent item
for i in dict1:
    if value==dict1[i]:
        print("2nd frequent item is", i)
        break
       


