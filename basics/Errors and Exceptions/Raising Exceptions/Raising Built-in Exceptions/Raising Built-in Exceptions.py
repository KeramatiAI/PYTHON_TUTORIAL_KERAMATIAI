"""Raising Built-in Exceptions
You can raise any built-in exception by creating an instance of the exception class and using the raise statement. Following is the syntax −

raise Exception("This is a general exception")
Example
Here is an example where we raise a ValueError when a function receives an invalid argument −
"""
def divide(a, b):
   if b == 0:
      raise ValueError("Cannot divide by zero")
   return a / b

try:
   result = divide(10, 0)
except ValueError as e:
   print(e)
"""Following is the output of the above code −

Cannot divide by zero"""