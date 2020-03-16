# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 18:12:09 2020

@author: SHARI
"""

#Assuming that we have some email addresses in the "username@companyname.com" format, 
#please write program to print the company name of a given email address. Both user names and company names are composed of letters only. 
#Example: If the following email address is given as input to the program: john@google.com Then, the output of the program should be: google
string=input("enter email address")
index=0
for i in string:
    if i=='@':
        index_start=index+1
    elif i=='.':
        index_end=index
        break
    else:
        pass
    index=index+1
    
company_name=string[index_start:index_end]
print("company name:",company_name)