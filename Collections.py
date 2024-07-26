# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 19:20:11 2024

@author: atul.sharma
"""

print("chain map")

'''
several different dictionaries, you need to group and manage them as a single one.

'''

from collections import ChainMap, defaultdict, OrderedDict


d1 = {'a': 1, 'b': 2}  
d2 = {'c': 3, 'd': 4}  
d3 = {'e': 5, 'f': 6}  


res_dict=ChainMap(d1,d2,d3)

#print(res_dict)

#print(list(res_dict.keys()))

#print(res_dict.maps)

O_dict=OrderedDict(one=1,two=2)

D_dict=defaultdict(str,{'a':'A','b':'B'})


res=ChainMap(O_dict,D_dict)

print(res)


#chain map from keys

#print(ChainMap.fromkeys(res_dict))


#------------------------------------------------------------------------------
'''operations of chainmap'''


numbers = {"one": 1, "two": 2}
letters = {"a": "A", "b": "B"}

d1=ChainMap(numbers,letters)


print(d1['a'])



#incase of duplicate key will get the key value of first occurance

for_adoption = {"dogs": 10, "cats": 7, "pythons": 3}
vet_treatment = {"dogs": 4, "cats": 3, "turtles": 1}


d2=ChainMap(for_adoption,vet_treatment)


print(d2["dogs"]) #10


'''
The for loop iterates over the dictionaries in d2 and prints the first
occurrence of each key-value pair. 
'''

for key, value in d2.items():
    
    print(key,'->',value)

'''
Chain map supports mutation as well but it will also applicable on first 
occurance only

'''

numbers = {"one": 1, "two": 2}
letters = {"a": "A", "b": "B"}

d3=ChainMap(numbers,letters)


d3['c']="C"


print(d3)

#del d3['a'] #KeyError: "Key not found in the first mapping: 'a'"























