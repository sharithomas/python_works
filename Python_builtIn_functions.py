#Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. 
#But Python has a built-in document function for every built-in functions. 
#Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input() 


# built-in document function abs()
print(abs.__doc__)

#built-in document function  int()
print(int.__doc__)

# built-in document function  raw_input()

#For Python 3. x, use input(). For Python 2. x, use raw_input()
print(input.__doc__)



#Add document for your own function
def my_test_fun(bar):
    
    "Help for my test function."
    
    return bar

help(my_test_fun)