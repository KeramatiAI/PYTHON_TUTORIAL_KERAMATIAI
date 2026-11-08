"""
Closing a File in Python
We can close a file in Python using the close() method. Closing a file is an essential step in file handling to ensure that all resources used by the file are properly released. It is important to close files after operations are completed to prevent data loss and free up system resources.
"""
"""
Example
In this example, we open the file for writing, write data to the file, and then close the file using the close() method −
"""
file = open("example.txt", "w")
file.write("This is an example.")
file.close()
print ("File closed successfully!!")
"""
The output produced is as shown below −

File closed successfully!!
"""