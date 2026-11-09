"""
Reading and Writing to a File Using "r+" Mode
When a file is opened for reading (with 'r' or 'rb'), writing data is not possible unless the file is closed and reopened in a different mode. To perform both read and write operations simultaneously, we add the '+' character to the mode parameter. Using 'w+' or 'r+' mode enables using both write() and read() methods without closing the file.

The File object also supports the seek() function, which allows repositioning the read/write pointer to any desired byte position within the file.

Syntax
Following is the syntax for seek() method −

fileObject.seek(offset[, whence])
Parameters
offset − This is the position of the read/write pointer within the file.

whence − This is optional and defaults to 0 which means absolute file positioning, other values are 1 which means seek relative to the current position and 2 means seek relative to the file's end.

Example
The following program opens a file in 'r+' mode (read-write mode), seeks a certain position in the file, and reads data from that position −
"""
# Open the file in read-write mode
with open("foo.txt", "r+") as fo:
   # Move the read/write pointer to the 10th byte position
   fo.seek(10, 0)

   # Read 3 bytes from the current position
   data = fo.read(3)

   # Print the read data
   print(data)
"""
After executing the above code, we get the following output −

rat
"""