"""
Reading a File Using read() Method
The read() method is used to read the contents of a file in Python. It reads the entire content of the file as a single string. This method is particularly useful when you need to process the whole file at once.

Syntax
Following is the basic syntax of the read() method in Python −

file_object.read(size)
Where,

file_object is the file object returned by the open() function.
size is the number of bytes to read from the file. This parameter is optional. If omitted or set to a negative value, the method reads until the end of the file.
Example
In the following example, we are opening the file "example.txt" in read mode. We then use the read() method to read the entire content of the file −
"""
# Open the file in read mode
file = open('example.txt', 'r')

# Read the entire content of the file
content = file.read()

# Print the content
print(content)

# Close the file
file.close()
"""
After executing the above code, we get the following output −

welcome to Tutorialspoint.
"""