# -*- coding: utf-8 -*-
"""
Created on Tue May 19 18:34:49 2020

@author: SHARI
"""

#Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number
# is an even number. The numbers obtained should be printed in a comma-separated sequence on a single line.



def even_check():
    even_list=[]
    
    for num in range(1000,3000):
        flag=0
        n=num
        while num!=0:
            r=num%10
            if r%2==0:
                flag=1
            else:
                flag=0
                break;
            num=num//10
        if flag==1:
            even_list.append(n)
    return even_list
        
result=even_check()
for i in result:
    print(i,end=",")
        
        
            
            
    