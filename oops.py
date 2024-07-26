# -*- coding: utf-8 -*-
"""
Created on Wed May  8 20:38:49 2024

@author: AtulSwati
"""

print("oops")

#------------------------------------------------------------------------------

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

#------------------------------------------------------------------------------
#property decorator

class Portal:
    def __int__(self):
        self.__name=''
        
    @property
    def name(self):
        return self.__name
    
    @name.setter 
    def name(self,value):
        self.__name=value
        #print("hello")
    
    @name.deleter 
    def name(self):
        del self.__name


p=Portal()

#p.name("GeeksForGeeks")

p.name='geeks'

#print(p.name)



#------------------------------------------------------------------------------
#abstract class

from abc import ABC, abstractmethod


class Person(ABC):
    @abstractmethod
    def Name(self):
        pass
    
    
#p=Person()  can not instentiate the abstract class
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        