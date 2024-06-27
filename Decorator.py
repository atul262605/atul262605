# -*- coding: utf-8 -*-
"""
Created on Wed May  8 13:15:39 2024

@author: AtulSwati
"""

#python decorator

def decorator(f):
    def wraper_function():
        print("Before function call")
        f()
        print("After function call")
        
    return wraper_function 

def main():
    print("This is  a stand alone function")
    
main=decorator(main)

#main()

#------------------------------------------------------------------------------

#passing arguments to decorator function

def decoratorFunction(func):
    
    def wraperFunction(arg1,arg2):
        print("There are 2 argument passed", arg1,arg2)
        
        func(arg1,arg2)
        
        print("wraper function is ending here")
        
    return wraperFunction 

@decoratorFunction 
def my_func(arg1,arg2):
    print("My name is {1} {0} !!!, AMAT".format(arg1, arg2))
    
    
#my_func("Atul", "Sharma")

#------------------------------------------------------------------------------

# Decorator with arguments

def decoratorFuncWithArguments(d_args1,d_args2):
    
    print("There are 2 decorator arguments passed : ", d_args1,d_args2)
    
    def decoratorFunct(func_to_decorate):
        
        print("Inside decorator with passed d_args",d_args1,d_args2)
        
        def wraper_function(f_arg1,f_arg2):
            
            print("Inside wraper function with function arguments", f_arg1,f_arg2)
            
            func_to_decorate(f_arg1,f_arg2)
            
        return wraper_function
    return decoratorFunct


@decoratorFuncWithArguments("d_args1", "d_args2")
def my_func(f_arg1,f_arg2):
    
    print("Inside main function with arguments : ", f_arg1,f_arg2)
    

#my_func("Atul", "Sharma")


#------------------------------------------------------------------------------

res_matrix=[[col for col in range(5)] for row in range(5)]

print(res_matrix)




