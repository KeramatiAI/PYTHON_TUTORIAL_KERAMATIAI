"""Python Try-Finally Block
In Python, the try-finally block is used to ensure that certain code executes, regardless of whether an exception is raised or not. Unlike the try-except block, which handles exceptions, the try-finally block focuses on cleanup operations that must occur, ensuring resources are properly released and critical tasks are completed.

Syntax
The syntax of the try-finally statement is as follows −

try:
   # Code that might raise exceptions
   risky_code()
finally:
   # Code that always runs, regardless of exceptions
   cleanup_code()
In Python, when using exception handling with try blocks, you have the option to include either except clauses to catch specific exceptions or a finally clause to ensure certain cleanup operations are executed, but not both together.
Example
Let us consider an example where we want to open a file in write mode ("w"), writes some content to it, and ensures the file is closed regardless of success or failure using a finally block −
"""
try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
finally:
   print ("Error: can\'t find file or read data")
   fh.close()
"""If you do not have permission to open the file in writing mode, then it will produce the following output −

Error: can't find file or read data
The same example can be written more cleanly as follows −
"""
try:
   fh = open("testfile", "w")
   try:
      fh.write("This is my test file for exception handling!!")
   finally:
      print ("Going to close the file")
      fh.close()
except IOError:
   print ("Error: can\'t find file or read data")
"""When an exception is thrown in the try block, the execution immediately passes to the finally block. After all the statements in the finally block are executed, the exception is raised again and is handled in the except statements if present in the next higher layer of the try-except statement."""