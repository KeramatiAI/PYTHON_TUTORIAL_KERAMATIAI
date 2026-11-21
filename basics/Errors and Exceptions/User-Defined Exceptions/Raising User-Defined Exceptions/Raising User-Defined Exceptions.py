"""Raising User-Defined Exceptions
Once you have defined a custom exception, you can raise it in your code to signify specific error conditions. Raising user-defined exceptions involves using the raise statement, which can be done with or without custom messages and attributes.

Syntax
Following is the basic syntax for raising an exception −

raise ExceptionType(args)
Example
In this example, the "set_age" function raises an "InvalidAgeError" if the age is outside the valid range −
"""
def set_age(age):
   if age < 18 or age > 100:
      raise InvalidAgeError(age)
   print(f"Age is set to {age}")
