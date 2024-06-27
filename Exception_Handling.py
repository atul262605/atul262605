# -*- coding: utf-8 -*-
"""
Created on Thu May  2 12:17:47 2024

@author: AtulSwati
"""

print("exception handing")

try:
    test_list=[1,2,3]
    
    #print(test_list[9])
    print(test_list[0])
    #print(1/0)
    #print(res)

except IndexError as e:
    print("out of index")
    print(e)
except ZeroDivisionError as e:
    print(e)
except NameError as e:
    print(e)
    
else:
    print("This block will run if try block able to execute without any error")
    
finally:
    print("This code always execute")


#Can I get the exception from the finally block in python?
import sys

#class need to be creted for custom exceptions

class ValueException(Exception):
    pass 

def func(i):
    
    try: 
        if i==1:
            raise ValueException
    except ValueException:
        print(" except -->"+str(sys.exc_info()))
    finally:
        print("finally")
func(0)
func(1)
 



class On_Key(Exception):
    pass
class On_Message(Exception):
    pass
class On_Timer(Exception):
    pass


def caone_func(msg):
    
    try:
        if type(msg) == On_Key:
            raise On_Key


    except On_Key:
        print("On key Event is raised")



obj_k=On_Key()

caone_func(obj_k)




















