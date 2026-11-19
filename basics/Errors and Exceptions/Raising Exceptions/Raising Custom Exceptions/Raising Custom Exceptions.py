"""Raising Custom Exceptions
In addition to built-in exceptions, you can define and raise your own custom exceptions by creating a new exception class that inherits from the base Exception class or any of its subclasses −
"""
class MyCustomError(Exception):
   pass

def risky_function():
   raise MyCustomError("Something went wrong in risky_function")

try:
   risky_function()
except MyCustomError as e:
   print(e)
"""Output of the above code is as shown below −

Something went wrong in risky_function
Creating Custom Exceptions"""