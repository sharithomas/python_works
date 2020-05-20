# -*- coding: utf-8 -*-
"""
Created on Mon May 18 11:02:47 2020

@author: SHARI
"""

#Write a program that computes the net amount of a bank account based a transaction log from console input. 
#The transaction log format is shown as following: D 100 W 200 D means deposit while W means withdrawal. 
#Suppose the following input is supplied to the program: D 300 D 300 W 200 D 100 Then, the output should be: 500

deposit,withdrawal=0,0
while True:
    log=input("enter transaction log in D/W format\n")
    if log=="":
        break
    else:
        log=log.split(" ")
        if log[0]=="D":
            deposit=deposit+int(log[1])
        elif log[0]=="W":
            withdrawal=withdrawal+int(log[1])

print("Net Amount=",deposit-withdrawal)
        
