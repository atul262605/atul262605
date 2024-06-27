# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 23:07:51 2024

@author: atul.sharma
"""

import os

out=os.path.basename('C:/Users/atul.sharma/Downloads/Atul Documents/Applied Materials')

print(out)

base=os.path.dirname('C:/Users/atul.sharma/Downloads/Atul Documents/Applied Materials')

print(base)


base=os.path.isabs('C:/Users/atul.sharma/Downloads/Atul Documents/Applied Materials')

base1=os.path.isabs('./Documents/python')

print(base)

print(base1)