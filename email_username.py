# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 14:40:18 2020

@author: SHARI
"""

#Assuming that we have some email addresses in the "username@companyname.com" format, 
#please write program to print the user name of a given email address.
# Both user names and company names are composed of letters only.
string=input("enter email address")
index=0
for i in string:
    if i=='@':
        index_end=index
        break
    index=index+1
    
#characters  till '@'  save as user name
username=string[:index_end]
#split domain name with '.'

print("username",username)