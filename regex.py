# -*- coding: utf-8 -*-
"""
Created on Tue May  7 10:20:02 2024

@author: AtulSwati
"""

import re

#print("regex")

test_string = '123abc456789abc123ABC'

pattern=re.compile(r'abc')

match=re.search(pattern, test_string) #first occurance of match

matches=re.findall(pattern, test_string) # return list of all match

sp=re.split(pattern, test_string) #split the string with given pattern

replace=re.sub(pattern,'***', test_string) #replace the string with given pattern

#print(matches)

#print(sp)

#print(replace)

matchs=re.finditer(pattern, test_string) #returns iteraor of match

#print(matchs) #iterator

for match in matchs:
    #print(match.group())
    pass

#---------------------------------------------------------------------------------

# Method on matched object

'''
group(): Return the string matched by the RE
start(): Return the starting position of the match
end(): Return the ending position of the match
span(): Return a tuple containing the (start, end) positions of the match
'''

test_string = '123abc456789abc123ABC'

pat = re.compile(r'123')

matches = re.finditer(pattern, test_string)


res=[]
for match in matches:
    
    res.append(match.group(0))
    #print(match)
    #print(match.group())
    #print(match.span(),match.start(),match.end())


#print(res)

#--------------------------------------------------------------------------------

# meta character

'''
.  : Any character  except new line

^hello : start with hello

\$ : ends with

* : zero or more 

+ : 1 or more occurance

{} : repeation 

[] : char set

\ :  escape sequence for scpecial character

| : or 

() : captures group

'''

test_string = 'python-engineer.com'

f = re.findall(r'\.\w+', test_string)

pattern = re.compile(r'([\w.-]+)\.(\w+)')

f_mail = re.search(pattern, test_string)

#print(f)

#print(f_mail.group())

#print(f_mail.group(1))

#print(f_mail.group(2))

#------------------------------------------------------------------------------
test_string = 'hello 123_ heyho hohey a123'


pattern = re.compile(r'\b\d+_?')

f =re.findall(pattern, test_string)

print(f)

#------------------------------------------------------------------------------

#\w : Matches any alphanumeric (word) character; this is equivalent to the class [a-zA-Z0-9_].

#\W : Matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_].

#\b : Returns a match where the specified characters are at the beginning or at the end of a 
#     word r"\bain" r"ain\b"

#\A or ^ :  Returns a match if the specified characters are at the beginning of the string "\AThe"

# \Z or $ : matches at the end of string

p_1=re.compile(r'\bhey')

f1=re.findall(p_1, test_string)

#print(f1)

p_2=re.compile(r'hey\b')

f2=re.findall(p_2, test_string)

#print(f2)


#------------------------------------------------------------------------------
test_str='''
01.04.2020

2020.04.01

2020-04-01
2020-05-23
2020-06-11
2020-07-11
2020-08-11

2020/04/02

2020_04_04
2020_04_04
2020\04\02
'''


pattern = re.compile(r'\d+[-._//]\d+[-._//]\d+')

matches = re.findall(pattern, test_str)

#print(matches)

#------------------------------------------------------------------------------
'''
* : 0 or more

? : optional

+ : 1 or more

{4} : exact number

{2,6} : repeatation in range

'''

pattern = re.compile(r'\d{4}[.-]?\d{2}[.-]?\d{2}')

matches = re.findall(pattern, test_str)

#print(matches)

#------------------------------------------------------------------------------


my_string = """
Mr Simpson
Mrs Simpson
Mr. Brown
Ms Smith
Mr. T
"""

#pattern = re.compile(r'(Mr|Mrs|Ms)\.?\s\w+')
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s\w+')

matches = re.findall(pattern, my_string)

#print(matches)

# matches = pattern.finditer(my_string)
# for match in matches:
#     print(match)


#------------------------------------------------------------------------------

emails = """
pythonengineer@gmail.com
Python-engineer@gmx.de
python-engineer123@my-domain.org
"""

pattern1 = re.compile('r[\w.-]+@[\w.-]+')

matches = re.finditer(pattern1, emails)

# for match in matches:
#     print(match)



urls = """
http://python-engineer.com
https://www.python-engineer.org
http://www.pyeng.net
"""


pat = re.compile(r'https?://[\w.-]+')

matches = re.finditer(pat,urls)


for match in matches:
    print(match)


#------------------------------------------------------------------------------

# diffrent re methods

test_str= 'foo123baar345baaz789foo-bar'

#search method

match = re.search(r'\d+', test_str)

if match:
    print(match)
    print(match.group())


# re.match    
match1= re.match(r'\d+',test_str)

if match1:
    print(match1)
else:
    print("match doest not found at start")


# re.fullmatch()
#re.fullmatch() returns a match only if <regex> matches <string> in its entirety:
    
#match2= re.fullmatch('\d+', test_str)

match2= re.fullmatch('[\w-]+', test_str)
if match2:
    print(match2)
else:
    print('entire string did not matched')


# re.findall()

match3 = re.findall(r'\d+',test_str)

if match3:
    print(match3)
    
# re.finditer()

match3 = re.finditer(r'\d+',test_str)

# if match3:
#     print(list(match3))
#     print(match3.)

for match in match3:
    print(match.group(0))

#re.findall() returns a list, whereas re.finditer() returns an iterator.

#-------------------------------------------------------------------------------

#Substitution Functions


# re.sub Scans a string for regex matches, replaces the matching portions of 
#        the string with the specified replacement string, and returns the result

test_str= 'foo123baar345baaz789foo-bar'

res= re.sub('\d+', '***', test_str)


#print(res)



resn = re.subn('\d+', '***', test_str,count=2)

#print(resn)


#------------------------------------------------------------------------------

# Utility function

# re.split()

res_list = re.split(r'\d+', test_str)

#print(res_list)

# max split
res_list = re.split(r'\d+', test_str, maxsplit=2)

#print(res_list)

#------------------------------------------------------------------------------

pattern = re.compile(r'ba+[r|z]')

result = re.findall(pattern, test_str)

#print(result)

#------------------------------------------------------------------------------

'''
Why Bother Compiling a Regex?

This enhances modularity
'''


















































