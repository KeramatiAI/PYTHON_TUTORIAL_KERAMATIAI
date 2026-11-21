"""Nested try Block in Python
In a Python program, if there is another try-except construct either inside either a try block or inside its except block, it is known as a nested-try block. This is needed when different blocks like outer and inner may cause different errors. To handle them, we need nested try blocks.

We start with an example having a single "try − except − finally" construct. If the statements inside try encounter exception, it is handled by except block. With or without exception occurred, the finally block is always executed.

Example 1
Here, the try block has "division by 0" situation, hence the except block comes into play. It is equipped to handle the generic exception with Exception class.
"""
a=10
b=0
try:
   print (a/b)
except Exception:
   print ("General Exception")
finally:
   print ("inside outer finally block")
"""It will produce the following output −

General Exception
inside outer finally block"""