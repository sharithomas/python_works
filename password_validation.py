# -*- coding: utf-8 -*-
"""
Created on Fri May 15 21:49:08 2020

@author: SHARI
"""

#Write a Python program to check the validity of password input by users.
#Validation :
#1.At least 1 letter between [a-z] and 1 letter between [A-Z].
#2.At least 1 number between [0-9].
#3.At least 1 character from [$#@].
#4.Minimum length 6 characters.
#5.Maximum length 12 characters.
#Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.
# Passwords that match the criteria are to be printed, each separated by a comma. Example If the following passwords are
# given as input to the program: ABd1234@1,a F1#,2w3E*,2We3345 Then, the output of the program should be: ABd1234@1
password_list=input("enter passwords:").split(",")
length=0
flag=0
special_ch=['$','#','@']
# function definition to check validty of each character of given password
def validity(ch):
    if ch.isdigit():
        flag=1
    elif ch.isalpha():
        flag=1
    elif ch in special_ch:
        flag=1
    else:
        flag=0
    return flag


password_valid=[]
for password in password_list:
    pass_len=len(password)
    validity_list=[]
    if (pass_len>=6) and (pass_len<=12):  #check length of password 
        length=1
    for i in password: # reading each character of password and save value 1 in validty_list if that character is valid else save 0
        validity_list.append(validity(i))
    if 0 not in validity_list:
        password_valid.append(password)
    else:
        pass
print("valid passwords are: ") 
for i in password_valid:
    print(i,end=",")
    
        

    
pass_len=len(password)
validity_list=[]
if (pass_len>=6) and (pass_len<=12):  #check length of password 
    length=1
    
for i in password: # reading each character of password and save value 1 in validty_list if that character is valid else save 0
   validity_list.append(validity(i))
if 0 not in validity_list:
    print("valid password")
else:
    print("Invalid password")