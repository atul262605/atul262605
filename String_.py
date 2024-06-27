# -*- coding: utf-8 -*-
"""
Created on Thu May  2 09:14:11 2024

@author: AtulSwati
"""

from collections import defaultdict, Counter
#from itertools import reduce
#------------------------------------------------------------------------------
#rotate first string to get another string
print(str)

test_str1 = 'geeks'
test_str2 = 'eksge'

for i in range(len(test_str2)):
    
    if test_str1[i:]+test_str1[:i]==test_str2:
        print(True)
        break

#------------------------------------------------------------------------------
#check either strings are anagram

s1 ="listen"
s2 ="silent"

d1=defaultdict(int)
d2=defaultdict(int)

for char in s1:
    d1[char]+=1

for char in s1:
    d2[char]+=1
    
#print(d1)
#print(d2)

if (all(d1[key]==d2[key] for key in d1)):
    print("Both strings are anagram")
else:
    print("not anagram !!!")
#------------------------------------------------------------------------------

#find all the palindrome in the string

string="ababa"

def IsPalindrome(str):
    if str[::-1]==str:
        return True
    else:
        False
        
def Find_All_Plindrome(str):
    
    res=[]
    
    for i in range(0,len(str)):
        for j in range(i+1,len(str)):
            
            if IsPalindrome(str[i:j+1]):
                res.append(str[i:j+1])
    return res


print(Find_All_Plindrome(string))

#------------------------------------------------------------------------------
#First string from the given array whose reverse is also present in the same array

str1 = ["geeks", "for", "skeeg"]

reversedmap={}

for word in str1:
    reversedmap[word]=word[::-1]

res={}
for word in str1:
    
    revword=word[::-1]
    
    if revword in reversedmap:
        print("True")
    else:
        res[revword]=word
        
#-----------------------------------------------------------------------------  

#Python – Replace duplicate Occurrence in String


s ='Gfg is best. Gfg also has Classes now. Classes help understand better.'

d={'Gfg':'It', 'Classes':'They'}

def Replace_Duplicate(test_str,repl_dict):
    
    s=set()
    test_list=test_str.split(' ')
    
    for idx, ele in enumerate(test_list):
        if ele in repl_dict:
            if ele in s:
                test_list[idx]=repl_dict[ele]
        else:
            s.add(ele)
    #print(res)
    return (test_list)

#print(Replace_Duplicate(s, d))

res=set()

test_list=s.split(' ')

for idx, ele in enumerate(test_list):
    if ele in d:
        if ele in res:
            test_list[idx]=d[ele]
        else:
            res.add(ele)
            
#print(" ".join(test_list))

#----------------------------------------------------------------------------- 
#Python – Replace all occurrences of a substring in a string
import re
test_str = "geeksforgeeks"
s1 = "geeks"
s2 = "abcd"

res=re.sub(s1,s2,test_str)

#print(res)

#------------------------------------------------------------------------------
#max occurance of string

test_str = "gfghsisbjknlmkesbestgfgsdcngfgcsdjnisdjnlbestdjsklgfgcdsbestbnjdsgfgdbhisbhsbestdkgfgb"
test_list = ['gfg', 'is', 'best']

res=[]
d={}
for ele in test_list:
    res.append(test_str.count(ele))
    
for ele in test_list:
    d[ele]=test_str.count(ele)

test = max(d, key= d.get)

#print(max(res))

#-------------------------------------------------------------------------------
#string methods

#str = "geeksforgeeks is for geeks"
test_str="geeks"
test_Str1="geesks2"

#print(len(str))

#print(str.count("geeks"))

#print(str.find("geeks")) #0
#print(str.find("geeks",1)) #8

#print(str.isalpha()) #False because of spaces   

#print(test_str.isalpha()) #True


#print(str.isalnum())

#print(test_str1.isalnum())

#print(test_str2.isalnum())


str_1= "_"
test_list = ( "geeks", "for", "geeks" ) 

res=str_1.join(test_list)

#print(res)

#print(str.rfind(test_str)) #gives last occurance of string

#string modification methods

#str.replace

test_str = "GeeksForGeeks"

new_str=test_str.replace('e',' ')

#print(new_str)

#str.translate : Remove char from the string
    
test_str = 'Geeks123For123Geeks'

new_str=test_str.translate({ord(i):None for i in '123'})

print(new_str)


#-------------------------------------------------------------------------------

#split the word on vowels



# vowel_str='aeiou'

# for char in test_str:
#     if char in vowel_str:
#         test_str=test_str.replace(char,'*')
        
#print(test_str.split('*'))

import re
test_str = 'GFGaBstuforigeeks'
pattern=re.compile(r'a|e|i|o|u')
res = re.split(pattern, test_str)

#print(res)

#-----------------------------------------------------------------------------

#check either  string is binary or not

string1 = "101011000111"
string2 = "201000001"

# try: 
#     int(string1,2)
    
# except ValueError:
#     print("string is not binary string")
    
# else:
#     print("string is binary string")
 
def Check_B_String(str):
    
    return all(char =='0' or char=='1' for char in str)
   
    
#print(Check_B_String(string2))
    
#-----------------------------------------------------------------------------
#Python program for removing i-th character from a string

string = "geeksFORgeeks"

i=4 

res=string[:i]+string[i+1:]

#print(res)



import string

#print(string.punctuation)

#------------------------------------------------------------------------------

#count number of digits in string

test_str = "geeks4feeks is No. 1 4 5 5geeks"

count=0
for char in test_str:
    if char.isdigit():
        count+=1


#print(count)

 
res=len(list(filter(lambda x:x.isdigit(),test_str)))

#print(res)

#------------------------------------------------------------------------------
#specifig char freqency list

test_str = "geeksforgeeks is best for geeks"
 

# char list 
char_list = ['e', 'b', 'g']


d={}
for char in test_str:
    if char in char_list:
        d[char]=d.get(char,0)+1
        
#print(d)

#------------------------------------------------------------------------------

#odd frequency char

test_str = 'geekforgeeks is best for geeks'

res=[char for char, count in Counter(test_str).items() if count&1] 

#print(res)

d=defaultdict(int)

for char in test_str:
    d[char]+=1
result=[]
for key in d:
    if d[key] &1:
        result.append(key)
        
       
#print(result)
#print(d)
r=(max(d,key=d.get)) 
m=min(d,key=d.get)      

#print(r,d[r])
#print(m,d[m])
#------------------------------------------------------------------------------
#substitute char with its occurance ***************

test_str = "geeksforgeeks is best for geeks"

repl_char='e'

count=1
res=''
#print(str(count))

for char in test_str:
    if char ==repl_char:
        res+=str(count)
        count+=1
         
    else:
        res+=char
 

#print(res)

#------------------------------------------------------------------------------
#Print Even and Odd Index Characters of a String – Python

test_str = 'geekforgeeks'

#print(list(enumerate(test_str)))

odd=[char for idx,char in enumerate(test_str) if idx & 1]
even=[char for idx,char in enumerate(test_str) if not (idx & 1)]

#print(odd)
#print(even)

#print(not (2&1)) 
 
#------------------------------------------------------------------------------

#Python – Characters Index occurrences in String


test_str = "gfg is best for geeks"

s=set()
res=defaultdict(list)

for idx, char in enumerate(test_str):
    if char != ' ':
        res[char].append(idx)
        s.add(char)
        
#print(res)

#print(s)

#------------------------------------------------------------------------------

from collections import OrderedDict

string='geeksforgeeks'

res=''.join((OrderedDict.fromkeys(string)) )

#print(res)



#print(''.join(OrderedDict.fromkeys(string)))



#----------------------------------------------------------------------------
#matching char in 2 strings

str1 = "aabcddekll12@"
str2 = "bb2211@55k"


res=[char for char in str1 if char in str2]


#print(len(res))


#-----------------------------------------------------------------------------
#Python Program to Accept the Strings Which Contains all Vowels

string = "SEEquoiaL"

test_str=string.lower()

vowels="aeiou"

res=all(vowel in test_str for vowel in vowels)

#print(res)


#------------------------------------------------------------------------------

# Find uncommon words in 2 strings

A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"


list_A=A.split()
list_B=B.split()

#print(list_A)
#print(list_B)



d=Counter(list_A+list_B)

#print(d)
res=[]
for key, value in d.items():
    if value==1:
        res.append(key)
        
#print(res)

#--------------------------------------------------------------------------

test_str='geeksforgeeks 33 is best'


res= len(''.join([char for char in test_str if char != ' ']))


#print(res)

#-----------------------------------------------------------------------------
#reverse the sentance

string = "geeks quiz practice code"

word_list=string.split()

#print(word_list)

#print(' '.join(word_list[::-1   ]))

#------------------------------------------------------------------------------

 
































