"""
Python User-defined Modules
Any text file with .py extension and containing Python code is basically a module. It can contain definitions of one or more functions, variables, constants as well as classes. Any Python object from a module can be made available to interpreter session or another Python script by import statement. A module can also include runnable code.

Creating a Python Module
Creating a module is nothing but saving a Python code with the help of any editor. Let us save the following code as mymodule.py
"""
# mymodule.py
def SayHello(name):
   print ("Hi {}! How are you?".format(name))
   return