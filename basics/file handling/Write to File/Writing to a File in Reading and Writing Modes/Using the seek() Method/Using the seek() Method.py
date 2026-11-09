"""
Using the seek() Method
The seek() method is used to set the position of the read/write pointer within the file. The syntax for the seek() method is as follows −

fileObject.seek(offset[, whence])
Where,

offset − This is the position of the read/write pointer within the file.

whence − This is optional and defaults to 0 which means absolute file positioning, other values are 1 which means seek relative to the current position and 2 means seek relative to the file's end.

Example
The following program demonstrates how to open a file in read-write mode ('w+'), write some data, seek a specific position, and then overwrite part of the file's content −
"""
# Open a file in read-write mode
fo = open("foo.txt", "w+")

# Write initial data to the file
fo.write("This is a rat race")

# Move the read/write pointer to the 10th byte
fo.seek(10, 0)

# Read 3 bytes from the current position
data = fo.read(3)

# Move the read/write pointer back to the 10th byte
fo.seek(10, 0)

# Overwrite the existing content with new text
fo.write('cat')

# Close the file
fo.close()
"""
If we open the file in read mode (or seek to the starting position while in 'w+' mode) and read the contents, it will show the following −

This is a cat race
"""