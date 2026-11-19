"""Using Else Clause with Try-Except Block
In Python, the else clause can be used in conjunction with the try-except block to specify code that should run only if no exceptions occur in the try block. This provides a way to differentiate between the main code that may raise exceptions and additional code that should only execute under normal conditions.

Syntax
Following is the basic syntax of the else clause in Python −

try:
   # Code that might raise exceptions
   risky_code()
except SomeExceptionType:
   # Handle the exception
   handle_exception()
else:
   # Code that runs if no exceptions occurred
   no_exceptions_code()
Example
In the following example −

If you enter a non-integer input, a ValueError will be raised, and the corresponding except ValueError block will handle it.
If you enter zero as the denominator, a ZeroDivisionError will be raised, and the corresponding except ZeroDivisionError block will handle it.
If the division is successful (i.e., no exceptions are raised), the else block will execute and print the result of the division.
"""
try:
   numerator = int(input("Enter the numerator: "))
   denominator = int(input("Enter the denominator: "))
   result = numerator / denominator
except ValueError:
   print("Error: Invalid input. Please enter valid integers.")
except ZeroDivisionError:
   print("Error: Cannot divide by zero.")
else:
   print(f"Result of division: {result}")
