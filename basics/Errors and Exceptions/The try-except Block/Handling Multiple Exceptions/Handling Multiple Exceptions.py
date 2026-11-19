"""Handling Multiple Exceptions
In Python, you can handle multiple types of exceptions using multiple except blocks within a single try-except statement. This allows your code to respond differently to different types of errors that may occur during execution.

Syntax
Following is the basic syntax for handling multiple exceptions in Python −

try:
   # Code that might raise exceptions
   risky_code()
except FirstExceptionType:
   # Handle the first type of exception
   handle_first_exception()
except SecondExceptionType:
   # Handle the second type of exception
   handle_second_exception()
# Add more except blocks as needed for other exception types
Example
In the following example −

If you enter zero as the divisor, a "ZeroDivisionError" will be raised, and the corresponding except ZeroDivisionError block will handle it by printing an error message.
If you enter a non-numeric input for either the dividend or the divisor, a "ValueError" will be raised, and the except ValueError block will handle it by printing a different error message.
"""
try:
   dividend = int(input("Enter the dividend: "))
   divisor = int(input("Enter the divisor: "))
   result = dividend / divisor
   print(f"Result of division: {result}")
except ZeroDivisionError:
   print("Error: Cannot divide by zero.")
except ValueError:
   print("Error: Invalid input. Please enter valid integers.")
