# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 11:29:35 2020

@author: SHARI
"""

#Define a custom exception class which takes a string message as attribute.

class MyCustomError(Exception): #exception class deefintion 
    def __init__(self,*args): #init method called automatically when instance of class created,It has *args in 
        #its arguments list. The *args is a special pattern matching mode that is used in functions and methods.
        # It allows multiple arguments to be passed, and stores the arguments passed as a tuple, but it
        #also allows no arguments to be passed at all.In our case, we are saying, that if any arguments are passed to the
        #MyCustomError constructor, we will take the first argument passed, and assign it to an attribute in the object 
        #called message. If no arguments are passed, None will be assigned to the message attribute.
        if args:
            self.message=args[0]
        else:
            self.message=None
    def __str__(self): #self method called when an instance is printed
        print("calling str")
        if self.message:
            return 'mycustom error,{0}'.format(self.message)
        else:
            return 'mycustom error has been raised'


raise MyCustomError #MyCustomError called without any argument
raise MyCustomError("we have a problem") # MyCustomError is passed with a string argument


