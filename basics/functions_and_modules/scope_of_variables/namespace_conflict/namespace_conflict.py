"""
Namespace Conflict in Python
If a variable of same name is present in global as well as local scope, Python interpreter gives priority to the one in local namespace.

Example
In the following example, we define a local and a global variable.
"""
marks = 50 # this is a global variable
def myfunction():
   marks = 70 # this is a local variable
   print (marks)

myfunction()
print (marks) # prints global value
"""
It will produce the following output −

70
50
"""