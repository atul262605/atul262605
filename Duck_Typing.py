# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 11:32:35 2024

@author: AtulSwati
"""
'''Duck typing in Python is a programming concept where the type or the class of 
an object is less important than the methods it defines. When you use duck typing, 
you do not check types at all. Instead, you check for the presence of a given method 
or attribute.'''


print("duck typing")

class Duck(object):
    def __init__(self):
        print("This is duck class")
    def Fly(self):
        print("Duck is flying")
    def Sound(self):
        print("Duck is making sound")
        
class swan(object):
    def Fly(self):
        print("swan is flying")
    def Sound(self):
        print("swan is making sound")
        
class Turkey(object):
    def Fly(self):
        print("Turkey is Flying")
    def Sound(self):
        print("Turkey is making sound")
        
objects=[Duck(),swan(),Turkey()]

try: 
    for obj in objects:
        pass
        obj.Fly()
        obj.Sound()
except TypeError:
    print("Object is not matching")
  
#------------------------------------------------------------------------------
      
from abc import ABC, abstractclassmethod

class Vehicle(ABC):
    def __init__(self, color, wheel_drive, trasmission):
        self.color=color
        self.wheel_drive=wheel_drive
        self.trasmission=trasmission
        
    @abstractclassmethod 
    def start(self):
        raise NotImplementedError("start() must be implemented")

    @abstractclassmethod
    def stop(self):
        raise NotImplementedError("start() must be implemented")
        
    @abstractclassmethod
    def Drive(self):
        raise NotImplementedError("start() must be implemented")
        
        
class Car(Vehicle):
    def start(self):
        print("car is starting")
    def stop(self):
        print("car is stoping")
    def Drive(self):
        print("car is driving")
        
class Truck(Vehicle):
    def start(self):
        print("Truck is starting")
    def stop(self):
        print("Truck is stoping")
    def Drive(self):
        print("Truck is driving")
class Jeep(Vehicle):
    def start(self):
        print("Jeep is starting")
    def stop(self):
        print("Jeep is stoping")
    def Drive(self):
        print("Jeep is driving")   
        
objs=[
      Car("Red",2,"AT"),
      Truck("Yellow",2,"MT"),
      Jeep("Blue",2,"AT")
      ]

for obj in objs:
    obj.start()
    obj.Drive()
    obj.stop()

#------------------------------------------------------------------------------    
#usage of super

class Vehicle(object):
    def __init__(self, color, wheel_drive, trasmission):
        self.color=color
        self.wheel_drive=wheel_drive
        self.trasmission=trasmission
    def get_color(self):
        return self.color
    def get_wheel_drive(self):
        return self.wheel_drive
    def get_transmission(self):
        return self.wheel_drive

class Car(Vehicle):
    def __init__(self, color, wheel_drive, trasmission,VIN):
        
        super().__init__(color, wheel_drive, trasmission)
        self.VIN = VIN
            
    @classmethod
    def factor_method(cls,str_v):
        color,wheel_drive,trasmission,VIN=str_v.split('-')
        return Car(color,wheel_drive,trasmission,VIN)
        
        
str1="Blue-2D-MT-678AT900"  
   
obj=Car("Red","4D","AT","123AT345")

obj2=Car.factor_method(str1)

 
print(obj.get_color())  

print(obj2.get_color())  
    
#----------------------------------------------------------------------------------    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    