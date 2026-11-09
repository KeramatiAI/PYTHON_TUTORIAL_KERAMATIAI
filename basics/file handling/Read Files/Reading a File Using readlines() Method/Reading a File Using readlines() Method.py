"""
Reading a File Using readlines() Method
The readlines() method reads all the lines from a file and returns them as a list of strings. Each string in the list represents a single line from the file, including the newline character at the end of each line.

This method is particularly useful when you need to process or analyse all lines of a file at once.

Syntax
Following is the basic syntax of the readlines() method in Python −

file_object.readlines(hint)
Where,

file_object is the file object returned by the open() function.
hint is an optional parameter that specifies the number of bytes to read. If specified, it reads lines up to the specified bytes, not necessarily reading the entire file.
Example
In this example, we are opening the file "example.txt" in read mode. We then use the readlines() method to read all the lines from the file and return them as a list of strings −
"""
# Open the file in read mode
file = open('example.txt', 'r')

# Read all lines from the file
lines = file.readlines()

# Print the lines
for line in lines:
   print(line, end='')

# Close the file
file.close()
"""
Output of the above code is as shown below −

welcome to Tutorialspoint.
Hi Surya.
How are you?.
"""