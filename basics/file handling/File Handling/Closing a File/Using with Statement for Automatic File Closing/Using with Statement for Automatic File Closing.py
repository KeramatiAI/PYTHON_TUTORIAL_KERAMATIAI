"""
Using "with" Statement for Automatic File Closing
The with statement is a best practice in Python for file operations because it ensures that the file is automatically closed when the block of code is exited, even if an exception occurs.

Example
In this example, the file is automatically closed at the end of the with block, so there is no need to call close() method explicitly −
"""
with open("example.txt", "w") as file:
   file.write("This is an example using the with statement.")
   print ("File closed successfully!!")
"""
Following is the output of the above code −

File closed successfully!!
"""