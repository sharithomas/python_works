# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 11:14:16 2020

@author: SHARI
"""

window=list(range(0,1000))
for x in range(0,1000):
    window[x]=0 # all windows closed intially


for s in range(1,1001): 
    for w in range(1,1001):
        if w%s ==0:  #checking for multiplies of w,, and open windows if closed else close if opened
            if window[w-1]==0: 
                window[w-1]=1
            else:
                window[w-1]=0
        else:
            pass
        
        
count=0
print("open windows are ")
for i in range(0,1000):
    if window[i]==1: #count open windows 
        count =count+1
        print (i+1)
print("total number of open windows are",count)

