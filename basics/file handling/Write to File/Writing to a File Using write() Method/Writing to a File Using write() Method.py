"""
Writing to a File Using write() Method
The write() method is used to write a single string to a file. This makes it suitable for various text-based file operations.

The write() method takes a single argument: the string that you want to write to the file. It writes the exact content of the string to the file without adding any additional characters, such as newlines.

Example
In the following example, we are opening the file "example.txt" in write mode. We then use the write() method to write a string to the file −
"""
# Open a file in write mode
with open("example.txt", "w") as file:
   file.write("Hello, World!\n")
   file.write("This is a new line.\n")
print ("File opened successfully!!")
"""
Following is the output of the above code −

File opened successfully!!
"""