"""The Finally Clause
The finally clause provides a mechanism to guarantee that specific code will be executed, regardless of whether an exception is raised or not. This is useful for performing cleanup actions such as closing files or network connections, releasing locks, or freeing up resources.

Syntax
Following is the basic syntax of the finally clause in Python −

try:
   # Code that might raise exceptions
   risky_code()
except SomeExceptionType:
   # Handle the exception
   handle_exception()
else:
   # Code that runs if no exceptions occurred
   no_exceptions_code()
finally:
   # Code that always runs, regardless of exceptions
   cleanup_code()
Example
In this example −

If the file "example.txt" exists, its content is read and printed, and the else block confirms the successful operation.
If the file is not found (FileNotFoundError), an appropriate error message is printed in the except block.
The finally block ensures that the file is closed (file.close()) regardless of whether the file operation succeeds or an exception occurs.
"""
try:
   file = open("example.txt", "r")
   content = file.read()
   print(content)
except FileNotFoundError:
   print("Error: The file was not found.")
else:
   print("File read operation successful.")
finally:
   if 'file' in locals():
      file.close()
   print("File operation is complete.")
