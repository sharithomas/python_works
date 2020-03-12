# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 15:12:19 2020

@author: SHARI
"""

#Please write a program which accepts basic mathematic expression from console and print the evaluation result. 
#Example: If the following string is given as input to the program: 35+3 Then, the output of the program should be: 38
print("enter mathematical expression")
expr=input()
operator_list=[]
operand=[]
#extracting operator and save in operator_list ie,12+3 then '+' will extract here
for x in expr:
    if x=='+' or x=='-' or x=='/' or x=='%' or x=='*':
        operator_list.append(x)

operator=operator_list[0]
#function to seperate operands and assiging to operand list from 12+3 , 12 and 3 extracting        
def split_operand(expr,operator):
    operand=expr.split(operator)
    return operand

#call to function split_operand  
operand=split_operand(expr,operator)
a=int(operand[0]) # 1st operand in a 
b=int(operand[1]) # 2nd operand in b

#call to function cal_expr
def cal_expr(a,b,operator):
    if operator=='+':
        return(a+b)
    elif operator=='-':
        return(a-b)
    elif operator=='*':
        return(a*b)
    elif operator=='/':
        return(a/b)
    elif operator=='%':
        return(a%b)
    else:
        pass
result=cal_expr(a,b,operator)
print("value of {} is {} ".format(expr,result))


