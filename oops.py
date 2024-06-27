# -*- coding: utf-8 -*-
"""
Created on Wed May  8 20:38:49 2024

@author: AtulSwati
"""

print("oops")

#Private Attributes in Python Classes

class Person():
     def __init__(self,name,age):
         self.__private="This is private attribute"
         self.name=name
         self.age=age
         self._protected="This is protected attribute"
         
     def display(self):
        print(self.__private)
        
obj=Person("Atul", 35)

#obj.display()

#protected attribute

class Employee(Person):
    
    def protected_Attribute(self):
        print(self._protected)
    

Emp=Employee("Atul", 40)

print(Emp._protected)

p=Person("Swati", 40)

print(p._protected)