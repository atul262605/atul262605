# -*- coding: utf-8 -*-
"""
Created on Sat May  4 08:22:35 2024

@author: AtulSwati
"""



'''

Text File: 
    Text file usually we use to store character data. For example, test.txt

Binary File: 
    The binary files are used to store binary data such as images, video files, 
    audio files.

File Paths:
    Absolute path: which always begins with the root folder
 
    Relative path: which is relative to the program's current working directory
    
    
    The absolute path includes the complete directory list required to locate the file.
    
    For example, /user/Pynative/data/sales.txt is an absolute path to discover the 
    sales.txt. All of the information needed to find the file is contained in the path 
    string
    
    ../ represents parent directory
    ./ current directory

'''

#copying the files

import shutil
import os

src_path=r'.\test.txt'

dst_path=r'..\Python_Practice\test.txt'

shutil.copy(src_path, dst_path)

#rename the file
old_name=r'..\Python_Practice\test.txt'

new_name=r'..\Python_Practice\test11.txt'

#os.rename(old_name,new_name)


#------------------------------------------------------------------------------

#count number of lines in file

number_of_lines=0
with open(r'test.txt','r') as fd:
    
    number_of_lines=len(fd.readlines())
    
    
#print(number_of_lines)



#exclude the blank lines
count=0
with open(r'test.txt','r') as fd:
     for line in  fd:
         if line.strip():
             count+=1


#print(count)

#------------------------------------------------------------------------------

# Redirect print output to files



with open(r'test1.txt','r+') as fd:
    print("Hello World !!!",file=fd)


#------------------------------------------------------------------------------

# readline()


with open(r'test.txt','r+') as f:
    line=f.readline()
    
    #print(line)
    
    while line !='':
        #print(line) 
        line=f.readline()
        


# reading first and last line using readline()

with open(r'test.txt','r+') as f:
    first_line=f.readline()
    
    for line in f:
        pass
    last_line=line
    
#print(first_line)
#print(last_line)

#------------------------------------------------------------------------------

# readlines() :  reading file into list

with open(r'test.txt','r+') as f:
    
    line=f.readlines()
    
print(line)


#------------------------------------------------------------------------------

# reading writing same file


with open(r'test.txt','r+') as f:
    
    print(f.read())
    
    #f.write('\n6. sixth line')




#------------------------------------------------------------------------------

#list all the files in directory

'''
os.listdir(path) : list all the files and directories 

The os.listdir(dir_path) will list files only in the current directory and 

ignore the subdirectories.

'''
#current working directory

#print(os.listdir())




dir_path=r'C:\Users\atul.sharma\Documents'

relative_dir_path = r'..\\' #represents parent directory

res=[]


for file_path in os.listdir(dir_path):
    
    #print(file_path)
    if os.path.isfile(os.path.join(dir_path,file_path)):
        
        res.append(file_path)  
        
    
#print(res,'\n')   



res1=[]
for file_path in os.listdir(relative_dir_path):
    
    #print(file_path)
    if os.path.isfile(os.path.join(relative_dir_path,file_path)):
        
        res1.append(file_path)  
        
    
#print(res1)   

#------------------------------------------------------------------------------

'''
os.walk():
    os.walk() function in Python to get a list of files in a directory and all
    
    of its subdirectories/subfolders.
    
    os.walk(top, topdown=True, onerror=None, followlinks=False)
    
    it yields a 3-tuple (dirpath, dirnames, filenames).
    
    os.walk returns generator that creates tuple of values
    
'''

dir_path=r'C:\Users\atul.sharma\Documents'

file_list=[]
for dirpath, dirname, filename in os.walk(dir_path):
    
    for name in filename:
        if name.endswith('.py'):
            file_list.append(name)
    
    #print(dirpath)
    


#print(file_list)

#------------------------------------------------------------------------------
#Move Files Or Directories in Python

import shutil

    
src_p=r'C:\Users\atul.sharma\Documents\get-pip.py'
dst_p=r'.\\'



#shutil.move(src_p, dst_p)



#------------------------------------------------------------------------------

#split the dir path and file name
# split file name and extension

dir_pat,file_name=os.path.split(src_p)


#print(dir_pat,file_name)


file,extension= os.path.splitext(file_name)

#print(file,extension)

#------------------------------------------------------------------------------
#
#Move File and Rename

src_p=r'C:\Users\atul.sharma\Documents\get-pip.py'
dst_p=r'C:\Users\atul.sharma\Documents'


dir_path, file_name=os.path.split(src_p)

file,extension=os.path.splitext(file_name)


new_file_name= os.path.join(file+'_new'+extension)

#print(new_file_name)


dst_p=os.path.join(dst_p+new_file_name)

#print(dst_p)

#shutil.move(src_p, dst_p)

#------------------------------------------------------------------------------



src_p=r'C:\Users\atul.sharma\Documents\test_dir\\'
dst_p=r'C:\Users\atul.sharma\Documents\python\\'



for file_name in os.listdir(src_p):
    
    #print(file_name)
    src_folder=src_p+file_name
    dst_folder=dst_p+file_name
    
    #print(src_folder)
    #print(dst_folder)
    
    if os.path.isfile(src_folder):
        #shutil.move(src_folder, dst_folder)
        #print('moved:',file_name)
        pass

#------------------------------------------------------------------------------


import glob

#glob.glob(pathname, *, recursive=False)   

dst_p=r'C:\Users\atul.sharma\Documents\python\\'

pattern= '*.py'
for file_name in glob.glob(dst_p+pattern):
    #print(os.path.basename(file_name))   
    pass











