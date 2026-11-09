"""
Reading a File Using readline() Method
The readline() method is used to read one line from a file at a time. This method is useful when you need to process a file line by line, especially for large files where reading the entire content at once is not practical.

Syntax
Following is the basic syntax of the readline() method in Python −

file_object.readline(size)
Where,

file_object is the file object returned by the open() function.
size is an optional parameter specifying the maximum number of bytes to read from the line. If omitted or set to a negative value, the method reads until the end of the line.
Example
In the example below, we are opening the file "example.txt" in read mode. We then use the readline() method to read the first line of the file −
"""
# Open the file in read mode
file = open('example.txt', 'r')

# Read the first line of the file
line = file.readline()

# Print the line
print(line)

# Close the file
file.close()
"""
Following is the output of the above code −

welcome to Tutorialspoint.
"""