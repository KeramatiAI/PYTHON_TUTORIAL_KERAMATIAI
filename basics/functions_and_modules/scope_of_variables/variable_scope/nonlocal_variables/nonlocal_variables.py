"""
Nonlocal Variables
The Python variables that are not defined in either local or global scope are called nonlocal variables. They are used in nested functions.

Example
The following example demonstrates the how nonlocal variables works.
"""
def yourfunction():
   a = 5
   b = 6
   # nested function
   def myfunction():
      # nonlocal function
      nonlocal a
      nonlocal b
      a = 10
      b = 20
      print("variable a:", a)
      print("variable b:", b)
      return a+b
   print (myfunction())
yourfunction()
"""
The above code will produce the below output −

variable a: 10
variable b: 20
30
"""