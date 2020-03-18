# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 10:04:09 2020

#@author: SHARI
"""

#Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is
#  in ["Hockey","Football"].Hints: Use list[index] notation to get a element from a list.

n=int(input("enter size"))
#function to accept subject, verb and object as different list
def input_details(list_in,n):
    list_in=[]
    for i in range(n):
        list_in.append(input())
    return list_in

print("enter all subjects of sentences")
#call to fumction to generate subject list
subject=input_details(list_in,n)
print("enter all verbs of sentences")

#call to fumction to generate verb list
verb=input_details(list_in,n)
print("enter all objects of sentences")

#call to fumction to generate object list
object_in=input_details(list_in,n)
 
print("all sentences in order:")
#print all sentences
for i in range(n):
    print(subject[i]+"\t"+verb[i]+"\t"+object_in[i])