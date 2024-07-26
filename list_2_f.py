# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 15:43:47 2021

@author: uidj1654
"""

print("Python object oriented")

 

class Person(object):
   def __init__(self,first_name,last_name,age):
      self.first_name=first_name
      self.last_name=last_name
      self.age=age
      
   def print_person_info(self):
      print("first name : {} , last name : {} , age : {}".format(self.first_name,self.last_name,self.age))
      
   @classmethod   
   def factory_method(cls,csv):
      first_name,last_name,age=csv.split('-')
      return cls(first_name,last_name,age)
   
   @staticmethod
   def age_verify(age):
      if age>=18:
         print("Person is adult")
      else:
         print("Person is undet age")
         
   def __private_method(self):
      print("This is the private method of class person")
         
p1=Person("atul","sharma",33)
p1.print_person_info()

p2=Person.factory_method("ashok-sharma-64")

p2.print_person_info()
p2.age_verify(int(p2.age))


'''Why are Python's 'private' methods not actually private?'''
#p1.__private_method()  'Person' object has no attribute '__private_method'

#Person.__private_method() AttributeError: type object 'Person' has no attribute '__private_method'   

                        
p1._Person__private_method()                  
                    
print(dir(p1))
'''
['_Person__private_method', '__class__', '__delattr__', '__dict__', '__dir__', 
'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
 '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
 '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
 '__subclasshook__', '__weakref__', 'age', 'age_verify', 'factory_method',
 'first_name', 'last_name', 'print_person_info'] 

The name scrambling is used to ensure that subclasses don't accidentally override 
the private methods and attributes of their superclasses. It's not designed to
 prevent deliberate access from outside.
''' 
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    