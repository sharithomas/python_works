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
        index_start=index
        break
    index=index+1
    
#string after '@' and save to domain
domain=string[index_start+1:]
#split domain name with '.'
company_name=domain.split('.')
print("company name:",company_name[0])
