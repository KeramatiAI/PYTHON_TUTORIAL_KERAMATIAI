"""
Global Variables
A global variable can be accessed from any part of the program, and it is defined outside any function or block of code. It is not specific to any block or function.

Example
The following example shows the scope of global variable. We can access them inside as well as outside of the function scope.
"""
#global variables
name = 'Davoud Keramati'
marks = 50
def myfunction():
   # accessing inside the function
   print("name:", name)
   print("marks:", marks)
# function call   
myfunction()
"""
The above code will produce the following output −

name: TutorialsPoint
marks: 50
"""