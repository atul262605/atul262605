# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 08:59:40 2021

@author: uidj1654
"""

print("MRO")

class A(object):
      def __init__(self):
         print("A's init method")
         
      def test(self):
         print("this is class A")
      
class B(A):
   pass

class C(object):
   def __init__(self):
      print("C's init method")
   def test(self):
      print("this is class C")
      
class D(B,C):
   def test(self):
      super(C,self).test(self)
    
      
#obj=D()

#obj.test()


class base(object):
   def __init__(self):
      print("this is base class")
      
   def test(self):
      print("hello world")
      
class derived(base):
   def __init__(self):
      print("This is derived class")
      super(derived,self).__init__()
      
   def test2(self):
      print("hello world !!!!!")
      
class child1(base):
   def __init__(self):
      print("This is child1 class")
      super(child1,self).__init__()
      
class grandchild(derived,child1):
   def __init__(self):
      print("This is grand child class")
      super(grandchild,self).test2( )
      derived.test(self)
      
   def test2(self):
      super(grandchild,self).test()
      #super(grandchild,self).test()
#d=derived()

#c1=child1()

g1=grandchild()
g1.test2()