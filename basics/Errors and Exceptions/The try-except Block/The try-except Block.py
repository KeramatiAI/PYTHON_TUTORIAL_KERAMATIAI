"""Python Try-Except Block
In Python, the try-except block is used to handle exceptions and errors gracefully, ensuring that your program can continue running even when something goes wrong. This tutorial will cover the basics of using the try-except block, its syntax, and best practices.

Exception handling allows you to manage errors in your code by capturing exceptions and taking appropriate actions instead of letting the program crash. An exception is an error that occurs during the execution of a program, and handling these exceptions ensures your program can respond to unexpected situations.
The try-except block in Python is used to catch and handle exceptions. The code that might cause an exception is placed inside the try block, and the code to handle the exception is placed inside the except block.

Syntax
Following is the basic syntax of the try-except block in Python −"""

"""try:
   # Code that might cause an exception
   risky_code()
except SomeException as e:
   # Code that runs if an exception occurs
   handle_exception(e)
Example
In this example, if you enter a non-numeric value, a ValueError will be raised. If you enter zero, a ZeroDivisionError will be raised. The except blocks handle these exceptions and prints appropriate error messages −
"""
try:
   number = int(input("Enter a number: "))
   result = 10 / number
   print(f"Result: {result}")
except ZeroDivisionError as e:
   print("Error: Cannot divide by zero.")
except ValueError as e:
   print("Error: Invalid input. Please enter a valid number.")
