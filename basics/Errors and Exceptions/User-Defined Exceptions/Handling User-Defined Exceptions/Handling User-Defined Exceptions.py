"""Handling User-Defined Exceptions
Handling user-defined exceptions in Python refers to using "try-except" blocks to catch and respond to the specific conditions that your custom exceptions represent. This allows your program to handle errors gracefully and continue running or to take specific actions based on the type of exception raised.

Syntax
Following is the basic syntax for handling exceptions −

try:
   # Code that may raise an exception
except ExceptionType as e:
   # Code to handle the exception
Example
In the below example, the "try" block calls "set_age" with an invalid age. The "except" block catches the "InvalidAgeError" and prints the custom error message −

try:
   set_age(150)
except InvalidAgeError as e:
   print(f"Invalid age: {e.age}. {e.message}")
"""