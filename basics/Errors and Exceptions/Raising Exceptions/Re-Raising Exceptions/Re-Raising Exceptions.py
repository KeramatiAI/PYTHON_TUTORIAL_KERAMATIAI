
"""Re-Raising Exceptions
Sometimes, you may need to catch an exception, perform specific actions (such as logging, cleanup, or providing additional context), and then re-raise the same exception to be handled further up the call stack

This is useful when you want to ensure certain actions are taken when an exception occurs, but still allow the exception to propagate for higher-level handling.

To re-raise an exception in Python, you use the "raise" statement without specifying an exception, which will re-raise the last exception that was active in the current scope.

Example
In the following example −

The process_file() function attempts to open and read a file.
If the file is not found, it prints an error message and re-raises the "FileNotFoundError" exception.
The exception is then caught and handled at a higher level in the call stack."""
def process_file(filename):
   try:
      with open(filename, "r") as file:
         data = file.read()
         # Process data
   except FileNotFoundError as e:
      print(f"File not found: {filename}")
    	# Re-raise the exception
      raise

try:
   process_file("nonexistentfile.txt")
except FileNotFoundError as e:
   print("Handling the exception at a higher level")
"""After executing the above code, we get the following output −

File not found: nonexistentfile.txt
Handling the exception at a higher level"""