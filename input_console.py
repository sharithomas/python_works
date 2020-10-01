# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 20:24:19 2020

@author: SHARI
"""

def input_console():
    count=0
    while(True):
        try: 
            data=int(input("please  enter an integer"))   
        except:
            count=count+1 # increment count by one if it enters except block and check if it exceed 5 times then exit from loop else continue with next iteration
            if count>5:
                print("limit exceed: more than 5 times")
                break
            print("please try again")
            continue
        else:
            print("entered number is: ",data)
            break
        finally:
            print("Finally block is executed!")

input_console()
    

