# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 19:21:43 2024

@author: atul.sharma
"""

print("cookbook Chapter1")

#move all the zero begining of the array

arr=[0,1,2,0,4,3,0,5,0]

j=0

for i in range(1,len(arr)):
    if not arr[i]:
        arr[j],arr[i]=arr[i],arr[j]
        j+=1
    
print(arr)

#move all the zero at the end of array

arr1 = [0,1,2,0,4,3,0,5,0]

n=len(arr1)

j=n-1
i=0
while(i<j):
    if not arr1[j]:
        j-=1
        continue

    if not arr1[i]:
        arr1[j], arr1[i] = arr1[i], arr1[j]
        j-=1
    i+=1
print(arr1)