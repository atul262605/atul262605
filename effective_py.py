# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 00:38:08 2024

@author: atul.sharma
"""

print("effective python")




visits = [15, 35, 80]

visit_list=[[15, 35, 80],[45, 23, 60],[17, 45, 90]]

def normalize(numbers):
    res=[]
    
    total=sum(numbers)
    
    for num in numbers:
        res.append(100*num/total)
        
    return res

# def read_line(data_path):
#     with open(data_path) as fd:
#         yield fd.readlines()
             

#print(normalize(visits))
        
# li=read_line('my_numbers.txt')

# print(li)

# print(list(li))
# print(list(li)) #it is already exhausted

def list_gen(data):
     for ele in data:
         yield ele
         
li=list_gen(visit_list)

final_res=[]

for ele in li:
    final_res.append(normalize(ele))

print(final_res)




































