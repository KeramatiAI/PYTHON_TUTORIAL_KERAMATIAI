"""
Reading and Writing to a File Simultaneously in Python
When a file is opened for writing (with 'w' or 'a'), it is not possible to read from it, and attempting to do so will throw an UnsupportedOperation error.

Similarly, when a file is opened for reading (with 'r' or 'rb'), writing to it is not allowed. To switch between reading and writing, you would typically need to close the file and reopen it in the desired mode.

To perform both read and write operations simultaneously, you can add the '+' character to the mode parameter. Using 'w+' or 'r+' mode enables both write() and read() methods without needing to close the file.

Additionally, the File object supports the seek() function, which allows you to reposition the read/write pointer to any desired byte position within the file.

Example
In this example, we open the file in 'r+' mode and write data to the file. The seek(0) method repositions the pointer to the beginning of the file −
"""
# Open the file in read-write mode
with open("foo.txt", "r+") as fo:
   # Write data to the file
   fo.write("This is a rat race")

   # Rewind the pointer to the beginning of the file
   fo.seek(0)

   # Read data from the file
   data = fo.read()
   print(data)

