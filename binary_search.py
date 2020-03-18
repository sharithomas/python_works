# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 19:59:43 2020

@author: SHARI
"""

#Please write a binary search function which searches an item in a sorted list. 
#The function should return the index of element to be searched in the list. Hints: Use if/elif to deal with conditions

list_in=[1,4,7,8,9,10,11,13,15,20,33,45,60,77,80]

element=int(input("enter element to search"))
start=0
end=len(list_in)-1

#function definition for binary search
def bin_search(list_in,start,end,element):
    if end>=start:
        #calculate  index of middle element
        mid=(start+end)//2
        #if middle element is equal o searching element 
        if list_in[mid]==element:
            return mid 
        #if middle element is less than searching element then start index=mid+1
        elif list_in[mid]<element:
            start=mid+1
            return bin_search(list_in,start,end,element)
        #else middle element is greater than searching element then end index=mid-1
        else:
            end=mid-1
            return bin_search(list_in,start,end,element)
    
    else:
        return -1
        
index=bin_search(list_in,start,end,element)
if index!=-1:
    print("element is present at index:",index)
else:
   print("element not present")

