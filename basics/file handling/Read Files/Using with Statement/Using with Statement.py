"""
Using "with" Statement
The "with" statement in Python is used for exception handling. When dealing with files, using the "with" statement ensures that the file is properly closed after reading, even if an exception occurs.

When you use a with statement to open a file, the file is automatically closed at the end of the block, even if an error occurs within the block.
Example
Following is a simple example of using the with statement to open, read, and print the contents of a file −
"""
# Using the with statement to open a file
with open('example.txt', 'r') as file:
   content = file.read()
   print(content)
"""
We get the output as follows −

welcome to Tutorialspoint.
Hi Surya.
How are you?.
"""