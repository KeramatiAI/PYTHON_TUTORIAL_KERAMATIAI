"""
Local Variables
A local variable is defined within a specific function or block of code. It can only be accessed by the function or block where it was defined, and it has a limited scope. In other words, the scope of local variables is limited to the function they are defined in and attempting to access them outside of this function will result in an error. Always remember, multiple local variables can exist with the same name.

Example
The following example shows the scope of local variables.
"""
def myfunction():
   a = 10
   b = 20
   print("variable a:", a)
   print("variable b:", b)
   return a+b

print (myfunction())
"""
In the above code, we have accessed the local variables through its function. Hence, the code will produce the following output −

variable a: 10
variable b: 20
30
"""