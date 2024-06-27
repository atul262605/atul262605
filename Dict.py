# -*- coding: utf-8 -*-
"""
Created on Wed May  1 21:41:34 2024

@author: AtulSwati
"""

#   print("dict")

#Sorting string using order defined by another string


from collections import Counter
pat = "asbcklfdmegnot"
str =  "eksge"

str_c=Counter(str)

res=[]

for char in pat:
    if char in str_c:
        res.append(char*(str_c[char]))
    
      
print(''.join(res)[::-1])

#------------------------------------------------------------------------------
#max and sorted function on dict with key

d = {'a': 100, 'b': 20, 'c': 50, 'd': 100, 'e': 80}

#print(max(d.items(), key=lambda x: x[1]))
# ('a', 100)

#print(min(d.items(), key=lambda x: x[0]))
# ('b', 20)

#print (dict(sorted(d.items(),key= lambda x:x[1]))) #by values
#print (dict(sorted(d.items(),key= lambda x:x[0]))) #by keys

#print(d) 

#------------------------------------------------------------------------------
#Dict methods


d = {'a': 100, 'b': 20, 'c': 50, 'd': 100, 'e': 80}

d['f']=900

#print(d)

d=dict(sorted(d.items(),key=lambda x:x[1]))

#print(d)


#setdefault -returns the value of a key (if the key is in dictionary). Else, it 
#inserts a key with the default value to the dictionary. and returns the 
# default value


res=d.setdefault('a',0) #this will return the corresponding value

res=d.setdefault('g',0) #this will return the default value as g is not there

#print(d)

#------------------------------------------------------------------------------

#update method : update the dict with the values of other dict

d2={'h':80,'i':90}

d1=d.update(d2)

#print(d1) #method returns nothing but update the existing dict
#print(d)


#------------------------------------------------------------------------------

#pop item : by default removes last key pair

# d1=d

# print(d1)

# print(d1.popitem())
# print(d1.popitem())


# print(d1)
#print(d)

#------------------------------------------------------------------------------

#get -  Dict.get(key, default=None)

#print(d.get('k',0))

#------------------------------------------------------------------------------

#fromkeys

''' fromkeys() function returns the dictionary with key mapped and specific value. 
It creates a new dictionary from the given sequence with the specific value.'''



test_list=['x','y','z','q','r','s']

 
d3=dict.fromkeys(test_list,-1)

# print(d3)

# d4={}

# d4=d3.copy()

# print(d4)

# print(d4.popitem())

# print(d4)
# print(d3)

#------------------------------------------------------------------------------

#test if all values are same
test_dict = {"Gfg": 5, "is": 5, "Best": 5}

test_val=list(test_dict.values())[0]  
res=all(value ==test_val for value in test_dict.values())

#print(res)

#------------------------------------------------------------------------------
#create nested dict  using given list
test_dict = {'Gfg' : 4, 'is' : 5, 'best' : 9} 
test_list = [8, 3, 2]

res_dict={}

dict_list=list(test_dict.items()) 

#print(dict(dict_list))
# params = [['width', 1920], ['height', 1080]]

# res={param[0]:param[1] for param in params}

# print(res)


# employees = [('alex', 35), ('michael', 24), ('stephan', 44)]

# print(dict(employees))

# print(dict(params))

# letters_mapping = ['ah', 'bi', 'bj', 'ak']

# print(dict(letters_mapping))

    


res={idx:{key:test_dict[key]} for idx, key in zip(test_list,test_dict)}

print(res)


res_dict={}
for key, value in zip(test_list,test_dict.items()):
    res_dict[key]=dict([value])


print(res_dict)


#-----------------------------------------------------------------------------

#list of tuple into dict

list_1 = [("Nakul", 93), ("Shivansh", 45), ("Samved", 65),
          ("Yash", 88), ("Vidit", 70), ("Pradeep", 52)]

# from collections import defaultdict

# res=defaultdict(list)

# for ele in list_1:
#     res[ele[0]].append(ele[1])
# print(res)

res=dict()

for name, score in list_1:
    
    res.setdefault(name,[]).append(score)


#print(res)

#-----------------------------------------------------------------------------
#Extract Key’s Value, if Key Present in List and Dictionary


# initializing list
test_list = ["Gfg", "is", "Good", "for", "Geeks"]
 
# initializing Dictionary
test_dict = {"Gfg" : 2, "is" : 4, "Best" : 6}

res=[]

for key in test_dict:
    if key in test_list:
        res.append(test_dict[key])

#print(res)

#-----------------------------------------------------------------------------

#Python – Remove keys with substring values

test_dict = {1 : 'Gfg is best for geeks', 2 : 'Gfg is good', 3 : 'I love Gfg'}

sub_list = ['love', 'good']

res={}

for key,value in test_dict.items():
    
    if not any(ele in value for ele in sub_list):
        
        res[key]=value


#print(res)

#------------------------------------------------------------------------------
#Python – Convert key-values list to flat dictionary


test_dict = {'gfg' : {'x' : 5, 'y' : 6}, 'is' : {'x' : 1, 'y' : 4},
                                      'best' : {'x' : 8, 'y' : 3}}

#from collections import defaultdict

res=[(key,tuple(test_dict[k][key] for k in test_dict)) for key in test_dict['gfg']]


#print(res)        

#-------------------------------------------------------------------------------

test_dict = {'Gfg' : 1, 'is' : 2, 'best' : 3, 'for' : 4, 'geeks' : 5, 'CS' : 6}

key_list=list(test_dict)

print(key_list)

print(list(test_dict.items()))

k=2

res=[]
for i in range(0,len(key_list),k):
    res.append(dict((list(test_dict.items())[i:i+k])))
    
     
#print(res)   

#------------------------------------------------------------------------------  
#sort the dict by key and value altogether

test_dict = {'gfg': [7, 6, 3], 
             'is': [2, 10, 3], 
             'best': [19, 4]}

# res=sorted(test_dict.items(),key=lambda x:x[1])    


# for key in res:
#     res[key]=sorted(res[key])




res={key:sorted(test_dict[key]) for key in sorted(test_dict)}
    
#print(res)

#------------------------------------------------------------------------------

#Python – Sort Dictionary by Values Summation
test_dict = {'Gfg' : [6, 7, 4], 'is' : [4, 3, 2], 'best' : [7, 6, 5]} 


res={key:sum(test_dict[key]) for key in test_dict}

#print(res)


res=sorted(res.items(),key=lambda x:x[1])

#print(res)

#------------------------------------------------------------------------------
#remove duplicate word in string

input1 = 'Python is great and Java is also great Python'


s=set()
res=[]
for word in input1.split():
    if word not in s:
        res.append(word)
        s.add(word)
    else:
        continue
        
print(' '.join(res))


#------------------------------------------------------------------------------
from collections import Counter
 
def possible_words(test_list,charset):
    
    char_Dict=Counter(charset)
    res=[]
    flag=False
    for word in test_list:
        wordDict=Counter(word)
        
        for key in wordDict:
                        
            if char_Dict[key]==wordDict[key]:
                flag=True
            else:
                flag=False
                break
                
        if flag==True:
            res.append(word)
    return res
            
            



# if __name__ == "__main__":
#     input = ['goo', 'bat', 'me', 'eat', 'goal', 'boy', 'run']
#     charSet = ['e', 'o', 'b', 'a', 'm', 'g', 'l','o']
    
#     #res=possible_words(input, charSet)
#     #print(res)

#-----------------------------------------------------------------------------
#winner of election
from collections import defaultdict
def winner(input1):
    
    d=defaultdict((int))
    
    for candidate in input1:
        
        d[candidate]+=1
    print(d)   
    winner=max(d.items(),key= lambda x:x[1])
    
    print(winner)
    
    


if __name__ == "__main__": 
    input =['john','johnny','jackie','johnny','johnny','john','john',
            'john','jackie','jamie','jamie',
            'john','johnny','jamie','johnny',
            'john'] 
    winner(input) 

#-----------------------------------------------------------------------------
#Python – Extract values of Particular Key in Nested Values

test_dict = {'Gfg' : {"a" : 7, "b" : 9, "c" : 12},
             'is' : {"a" : 15, "b" : 19, "c" : 20}, 
             'best' :{"a" : 5, "b" : 10, "c" : 2}}


key_1 ='b' #all value of b need to be extracted

res=[sub[key]  for sub in test_dict.values() for key in sub if key==key_1]

#print(res)
#------------------------------------------------------------------------------
#Python – Key with maximum unique value

test_dict = {"Gfg": [5, 7, 5, 4, 5],
             "is": [6, 7, 4, 3, 3],
             "Best": [9, 9, 6, 5, 5]}

d=dict()
for key in test_dict:
    d[key]=len(set(test_dict[key]))
    
res=max(d.items(),key=lambda x:x[0])
    
print(res)

unique_values=[(key,len(set(sub))) for key,sub in test_dict.items()]

print(unique_values)

max_key=max(unique_values,key= lambda x:x[1])

print(max_key)



# max_key=None

# max_length=0

# for key in test_dict:
#      if max_length< len(set(test_dict[key])):
#          max_length=len(set(test_dict[key]))
#          max_key=key
         
# print(max_key)      

#------------------------------------------------------------------------------

#find duplicate char in string

input_str = 'geeksforgeeks'

charset=set()
res=set()
for char in input_str:
    
    if char in charset:
        res.add(char)
        
    else:
        charset.add(char)


#print(res)

d=defaultdict(int)

for char in input_str:
    d[char]+=1

#print(d)
res=[]
for key,value in d.items():
    if value>1 and key not in res:
        res.append(key)
        
    
#print(res)  
    

#------------------------------------------------------------------------------

#

test_list = [4, 6, 6, 4, 2, 2, 4, 4, 8, 5, 8]
    
    
    
d=defaultdict(list)

for ele in test_list:
    
    d[ele].append(ele)
 
print(d) 
 
#------------------------------------------------------------------------------
#ordered dict


from collections import OrderedDict
input_1 = 'rengineers rock'
pattern = 'er'   
    
    
d=OrderedDict.fromkeys(input_1)

index=0

for key in d:
    
    if key== pattern[index]:
        index=index+1
    
    if index==len(pattern):
        print("true")
        break
 
#------------------------------------------------------------------------------

test_str = 'geekforgeeks best for geeks'

lookp_dict = {"best" : "good and better", "geeks" : "all CS aspirants"}       
    
    
res=[lookp_dict.get(ele,ele) for ele in test_str.split()] 
    
print(' '.join(res) )
    
    
#------------------------------------------------------------------------------

myDict = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}


d_value=dict(sorted(myDict.items(),key= lambda x:x[1])  )

print(d_value)
    
d_key=dict(sorted(myDict.items(),key= lambda x:x[0])    )

print(d_key)
    
#------------------------------------------------------------------------------

#sort nested dict

test_dict = {'Nikhil' : {'English' : 5, 'Maths' :  2, 'Science' : 14},
             'Akash' : {'English' : 15, 'Maths' :  7, 'Science' : 2},
             'Akshat' : {'English' : 5, 'Maths' :  50, 'Science' : 20}}

#from operator import itemgetter


res={ key : dict(sorted(sub_dict.items(),key=lambda x :x[1])) for key, sub_dict in test_dict.items()}
    
print('\n')
print(res)
    
#------------------------------------------------------------------------------

#Python – Sort dictionaries list by Key’s Value list index

test_list = [{"Gfg" : [6, 7, 8], "is" : 9, "best" : 10}, 
             {"Gfg" : [2, 0, 3], "is" : 11, "best" : 19},
             {"Gfg" : [4, 6, 9], "is" : 16, "best" : 1}]
K = "Gfg"
print('\n')
print('\n')

idx=2
d=sorted(test_list,key = lambda x:x[K][idx])

#print(d)
#------------------------------------------------------------------------------
test_str = 'gfg is best for geeks'

test_dict = {'geeks': 1, 'best': 6}

res=[]
for word in test_str.split():
    if word in test_dict:
        res.append(' ')
    else:
        res.append(word)


#print(' '.join(res))

res1=[word for word in test_str.split() if word not in test_dict]

#print(' '.join(res1))  

#------------------------------------------------------------------------------

#find duplicate value in dict

ini_dict = {'a':1, 'b':2, 'c':3, 'd':2}

d=defaultdict(list)

d1={}
for key, value in ini_dict.items():
    
    d[value].append(key)
    
#print(d)



for key,value in ini_dict.items():
    
    d1.setdefault(value,[]).append(key)

#print(d1)
#------------------------------------------------------------------------------

#replace word from dict
 

test_str = 'geekforgeeks best for geeks'

 
# lookup Dictionary
lookp_dict = {"best" : "good and better", "geeks" : "all CS aspirants"}

res=[]
for word in test_str.split():
    
    if word in lookp_dict:
        
        res.append(lookp_dict[word])
    else:
        res.append(word)

#print(' '.join( res)        )
    
    
res1=[lookp_dict.get(word,word) for word in test_str.split()]

#print( ' '.join(res1))

#-----------------------------------------------------------------------------

original = 'abcdefghijklmnopqrstuvwxyz'
reverse =  'zyxwvutsrqponmlkjihgfedcba'
dictChars = dict(zip(original,reverse))


print(dictChars)

input1 = 'paradox'

res=[]
k=3
for char in input1[k:]:
    res.append(dictChars[char])
    
#print(res)


res=input1[:k+1]+''.join(res)

print(res)



















