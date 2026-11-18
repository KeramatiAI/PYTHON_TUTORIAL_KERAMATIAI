"""
Example
This example tries to open a file where you do not have write permission, so it raises an exception −
"""
try:
   fh = open("testfile", "r")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")
"""
This produces the following result −

Error: can't find file or read data
"""