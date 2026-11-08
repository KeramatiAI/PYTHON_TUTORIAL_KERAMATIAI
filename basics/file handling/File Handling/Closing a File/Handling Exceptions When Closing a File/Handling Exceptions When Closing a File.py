"""
Handling Exceptions When Closing a File
When performing file operations, it is important to handle potential exceptions to ensure your program can manage errors gracefully.

In Python, we use a try-finally block to handle exceptions when closing a file. The "finally" block ensures that the file is closed regardless of whether an error occurs in the try block −
"""
try:
   file = open("example.txt", "w")
   file.write("This is an example with exception handling.")
finally:
   file.close()
   print ("File closed successfully!!")
"""
After executing the above code, we get the following output −

File closed successfully!!
"""