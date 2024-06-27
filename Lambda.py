# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 17:11:10 2024

@author: AtulSwati
"""

'''Lambda function :
 The def defined functions do not return anything if not explicitly returned whereas 
 the lambda function does return an object. The def functions must be declared in the 
 namespace. The def functions can perform any python task including multiple conditions, 
 nested conditions or loops of any level, printing, importing libraries, raising Exceptions, 
 etc.    
    
    '''

#Lambda Function to Check if value is in a List

test_list=[1,2,3,4,5,6,7,8]

v=8

res=lambda test_list,v: True if v in test_list else False

''' <function <lambda> at 0x000001A1E7C58F78> lambda always returns function object '''
print(res(test_list,v))
#-------------------------------------------------------------------------------------------------
test_list1=[1,3,5,7,9,2]

test_list2=[1,2,5,8,0,]


# Here x is input from test_list2 and it is checked in test_list1 
# this way we can do the comparison

res=list(filter(lambda x : x in test_list1 ,test_list2))

res1=list(filter(lambda x : x in test_list1 if x%2==0 else None ,test_list2))

#print(res)

#print(res1)
#-------------------------------------------------------------------------------------------------
#Python Lambda with underscore as an argument

print(lambda num:num%2) 
#<function <lambda> at 0x0000019B51E15948> it returns a function object

l=lambda _:True

#print(l(1)) # when we want specific output for every input
#-------------------------------------------------------------------------------------------------
#lambda function with if
'''
 A lambda function must have a return value for every valid input, we cannot 
 define it with if but without else as we are not specifying what will we 
 return if the if-condition will be false i.e. its else part.
without else part it will fail
'''
#square=lambda x:x**2 if x>0 # syntext error

square=lambda x:x**2 if x>0 else None

max=lambda a,b: a if a>b else b

#print(max(10, 20))
#-------------------------------------------------------------------------------------------------
#nested lambda function
# lambda variable : lambda variable evaluted Left --> Right

l_func=lambda a=2,b=3 :lambda c:a+b+c

square=lambda x:x**2

Product=lambda f,n:lambda x:f(x)*n

print(Product(square, 2)(10))   
#-------------------------------------------------------------------------------------------------

#Map function and Lambda expression in Python to replace characters

str = 'grrksfoegrrks'
c1 = 'e' 
c2 ='r'

print(''.join(list(map(lambda char :c1 if char==c2 else char,str))))

#-------------------------------------------------------------------------------------------------
#find all palindrome in list
my_list = ["geeks", "geeg", "keek", "practice", "aa"] 

res=list(filter(lambda str:str==str[::-1],my_list))

print(res)

#find all anagrams
from collections import Counter

str1 = "eegsk"

res1=list(filter(lambda str:Counter(str1)==Counter(str),my_list))

print(res1)

#-------------------------------------------------------------------------------------------------
#iteration with lambda

l1 = [4, 2, 13, 21, 5] 

res=list(map(lambda x:x**2 ,l1))

#print(res)
#-------------------------------------------------------------------------------------------------
'''
reduce :
    The left argument, x, is the accumulated value and the right argument, y, is the 
    update value from the iterable. 
    
    reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5)
    
    If the optional initializer is present, it is placed before the items of the 
    iterable in the calculation, and serves as a default when the iterable is empty.
    If initializer is not given and iterable contains only one item, the first item is 
    returned.
    
    reduce(lambda x,y: x*100*y,[1,2],3)
    
    (3*100*1)*100*2
'''
from functools import reduce

list=[0,1]

res=lambda n: reduce(lambda x,_:x+[x[-1]+x[-2]],range(n-2),[0,1])


print(res(6))


#------------------------------------------------------------------------------

'''
walrus operator

:=

'''

sample_data = [
    {"userId": 1,  "name": "rahul", "completed": False},
    {"userId": 1, "name": "rohit", "completed": False},
    {"userId": 1,  "name": "ram", "completed": False},
    {"userId": 1,  "name": "ravan", "completed": True}
]



for data in sample_data:
    
    if name := data.get("name"):
        print("found name",name)



'''
If a comprehension uses the walrus operator in the value part of the
comprehension and doesn’t have a condition, it’ll leak the loop variable into 
the containing scope 
'''

test_list=[1,2,56,24,12,7,9,8,15]

    
res=[last:=ele//2 for ele in test_list]

print(last)

'''
r leakage doesn’t happen for the loop variables from
comprehensions
'''

res=[ele//2 for ele in test_list]


#------------------------------------------------------------------------------

 

 








































 

 





