# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 13:41:26 2024

@author: atul.sharma
"""

import subprocess

#c=subprocess.run(['ls','-l'],shell=True)
#print(c)
'''
Using run() without passing check=True is equivalent to using call(),
which only returned the exit code from the process.
'''
complete = subprocess.run('echo $HoMe', shell=True)

#   print('return code :',complete.returncode)

c=subprocess.run(['dir'],shell=True)

#print(c)

'Error handling'

try:
    c=subprocess.run(['false'],shell=True,check=True)
except subprocess.CalledProcessError as e:
    print("Error :",e)
    
'''
Capturing output:
    The standard input and output channels for the process started by run() 
    are bound to the parent’s input and output. That means the calling program 
    cannot capture the output of the command. Pass PIPE for the stdout and 
    stderr arguments to capture the output for later processing.

0 = stdin

1 = stdout

2 = stderr

'''

import os

#print(os.system('dir'))

#-----------------------------------------------------------------------------

'''
Os.popen():
    open a pipe to or from the command. The return value is an open file object 
    connected to the pipe.
    os.popen() does the same thing as os.system except that it gives us a file
    like stream object that we can use to access standard input/output for that
    process
    
subprocess.check_call(args, *, stdin=None, stdout=None, stderr=None, shell=False)
'''
res=subprocess.call(['echo','$HOME'],shell=True,stdout=subprocess.PIPE)

#------------------------------------------------------------------------------

'''
subprocess.check_output():
    subprocess.check_output(args, *, stdin=None, stderr=None, 
                                 shell=False, universal_newlines=False)
    
    The standard input and output channels for the process started by call() 
    are bound to the parent's input and output. That means the calling program 
    cannot capture the output of the command. To capture the output, we can use 
    check_output() for later processing.
'''
    
res=subprocess.check_output(['tasklist'],shell=True)

#print(res)


'''
Popen():
    process creation and management in this module is handled by the Popen
        
    subprocess.Popen() executes a child program in a new process. On Unix, the 
    class uses os.execvp()-like behavior to execute the child program. On 
    Windows, the class uses the Windows CreateProcess() function.
'''



# class subprocess.Popen(args, bufsize=0, executable=None, 
#                        stdin=None, stdout=None, stderr=None, 
#                        preexec_fn=None, close_fds=False, 
#                        shell=False, cwd=None, env=None, universal_newlines=False, 
#                        startupinfo=None, creationflags=0)






#res=subprocess.Popen(['notepad'],shell=True)
























