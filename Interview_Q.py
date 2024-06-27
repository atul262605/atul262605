# -*- coding: utf-8 -*-
"""
Created on Wed May  1 21:44:25 2024

@author: AtulSwati
"""

test_str = '''Gfg is best . Gfg also has Classes now. 
                Classes help understand better . ''' 
                
test_list=test_str.split()

repl_dict={ 'Gfg':'It','Classes':'This'}

#print(test_list)

res=set()

for idx, ele in enumerate(test_list):
    
    if ele in repl_dict:
        if ele in res:
            test_list[idx]=repl_dict[ele]
        else:
            res.add(ele)
            
print(' '.join(test_list))

#------------------------------------------------------------------------------              
#two sum problem

test_list=[1,3,5,9,10,11,15,19]



target=20

def two_sum(test_list,target):
    
    hash_map={} #index:values
    
    for i in range(len(test_list)):
        if (target-test_list[i]) in hash_map.values():
            #print(hash_map)
            return True
        else:
            hash_map[i]=test_list[i]
    return False

#print(two_sum(test_list, target))

# return indices

def two_sum_i(test_list,target):
    
    hash_map={} #values:index
    res=[]
    for i,ele in enumerate(test_list):
        diff=target-ele
        if diff in hash_map:
            #print(hash_map)
            res.append((i,hash_map[diff]))
            
        else:
            hash_map[ele]=i
    return res
            

#print(two_sum_i(test_list, target))
#------------------------------------------------------------------------------

#max product sub array

test_list=[2,3,-2,5,10]

def max_product_sub(test_list):
    res=max(test_list)
    #print("res :",res)
    maxValue, minValue=1,1
    
    for ele in test_list:
        
        if ele==0:
            maxValue=1
            minValue=1
            continue
        
        temp=maxValue*ele
        
        maxValue=max(maxValue*ele,minValue*ele,ele)
        #print(maxValue)
        minValue=min(temp,minValue*ele,ele)
        #print(minValue)
        res=max(maxValue,res)
    return res
 
#print(max_product_sub(test_list))   
    
    
#------------------------------------------------------------------------------    
#check if array cotains the duplicate
test_list1=[1,3,4,6,0,3]

def check_Duplicate(test_list1):
    
    test_list1.sort()
    res=[]
    i=0
    while i<len(test_list1)-1:
        if test_list1[i]==test_list1[i+1]:
            #res.append((i,i+1))
            return res
        i+=1
    return False
        
#print(check_Duplicate(test_list1)) 

#solution with set

'''
hash_set=set()

for ele in test_list1:
    if ele in hash_set:
        print("True")
    else:
        hash_set.add(ele)
'''
#return index of element of same value

def Duplicate_index(test_list1):
    
    hash_map={} #element:index
    res=[]
    for i,ele in enumerate(test_list1):
        
        if ele in hash_map:
            res.append((hash_map[ele],i))
            return res
        else:
            hash_map[ele]=i
    return False
        
print(Duplicate_index(test_list1))
    
#------------------------------------------------------------------------------
#binary representation in python
a = 0b1010  # 10 in decimal
b = 0b1100  # 12 in decimal

# print(bin(a&b))

# print(bin(a>>1))

# print(bin(b<<1))

# print(bin(a-1))
# print(int(a-1))
# print(bin(a>>1))
# print(int(a>>1))

# print(bin((a-1)&a))
# print(int((a-1)&a))
n=16
p=17
'''check if number is power of 2'''

def pow(n):
    
    if n!=0 and n&(n-1)==0:
        return True
    else:
        return False
    
#print(pow(277))

#count the set bit in integer

def count_set_bit(n):
    count=0
    type(n)
    while (n):
         count +=not (n&1)
         n=n>>1
    return count
n=16
#print(count_set_bit(n))

#print(n>>1)
#------------------------------------------------------------------------------
print("Hello World !!")

#prime number in range with list comprehension

res=[x for x in range(1,51) if all(x%y !=0 for y in range(2,x))]

#print(res)

n=50

res1=[]
for x in range(1,n):
    for y in range(2,x):
        if x%y ==0:
            break
    else:
        res1.append(x)
 
            
#print(res1)
            
#------------------------------------------------------------------------------
'''for loop with else statement'''

list1=[1,2,3,4,5,7]

target=17

for num in list1:
    if num==target:
        #print("Target number found")
        break
else:
    #print("Number not found")
    
    pass
#------------------------------------------------------------------------------
 

test_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

k=3
res=[]
for i in range(0,len(test_list),k):
    res.append(test_list[i:i+k])
    
print(res)

'''Alternate slicing'''

res_0=[x for i,x in enumerate(test_list) if i%(2*k)<k]

res_1=[x for i,x in enumerate(test_list) if i%(2*k)>=k]

print(res_0)
print(res_1)
 
#------------------------------------------------------------------------------

print(bin(-10))
print(bin(10))
#------------------------------------------------------------------------------
#second max

list1 = [10, 20, 4, 45, 99,88,]

maximum=max(list1[0],list1[1])

second_max=min(list1[0],list1[1])

for i in range(2,len(list1)):
    
    if list1[i]>maximum:
        second_max=maximum
        maximum=list1[i]
    elif list1[i]>second_max and list1[i] !=maximum:
        second_max=list1[i]

#print(maximum,second_max)
    

#------------------------------------------------------------------------------
#setdefault

test_list=[1,2,5,8,2,8,1,9,5,0,2,0]

ele_indices=dict()

for idx,ele in enumerate(test_list):
    ele_indices.setdefault(ele,[]).append(idx)
    
print(ele_indices)
#------------------------------------------------------------------------------
    
test_list=[2,2,4,4,6,2,8,5,4,8,5,8]

from collections import defaultdict

d=defaultdict(list)

for ele in test_list:
    d[ele].append(ele)
    
print(d)
    
#------------------------------------------------------------------------------
test_list1=[5,6,6,6]

test_list2=[8,3,5,7]

d=defaultdict(list)

for ele in zip(test_list1,test_list2):
    d[ele[0]].append(ele[1])
print(d)
    
#------------------------------------------------------------------------------
    
test_list=['7$2','5$6']

res1=[ele.split('$')[0] for ele in test_list]

res2=[ele.split('$')[1] for ele in test_list]
    
    
print(res1)

print(res2)  
    
#0----------------------------------------------------------------------------

test_list=[4,5,2,4,2,6,7,1,4]
import string

from collections import OrderedDict

set1=list(OrderedDict.fromkeys(test_list))

print(set1)

temp={}

for idx,ele in enumerate(set1):
    temp[ele]=string.ascii_lowercase[(idx)]
    
res=[temp[ele] for ele in test_list]

print(res)
    
#----------------------------------------------------------------------------
#extract % from string

test_str='geeksforgeeks 20% is 100% way to get 20% success'

# res=test_str.replace('%','')    
    
# print(res) 
    

    
    














