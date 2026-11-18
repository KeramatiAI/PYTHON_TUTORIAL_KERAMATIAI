"""
Example
This example opens a file, writes content in the file and comes out gracefully because there is no problem at all.
"""
try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")
   fh.close()
"""
It will produce the following output −

Written content in the file successfully
However, change the mode parameter in open() function to "w". If the testfile is not already present, the program encounters IOError in except block, and prints following error message −

Error: can't find file or read data
"""