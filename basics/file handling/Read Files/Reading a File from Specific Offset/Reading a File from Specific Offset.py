"""
Reading a File from Specific Offset
We can set the he file's current position at the specified offset using the seek() method.

If the file is opened for appending using either 'a' or 'a+', any seek() operations will be undone at the next write.
If the file is opened only for writing in append mode using 'a', this method is essentially a no-op, but it remains useful for files opened in append mode with reading enabled (mode 'a+').
If the file is opened in text mode using 't', only offsets returned by tell() are legal. Use of other offsets causes undefined behavior.
Note that not all file objects are seekable.

Example
The following example demonstrates how to use the seek() method to perform simultaneous read/write operations on a file. The file is opened in w+ mode (read-write mode), some data is added, and then the file is read and modified at a specific position −
"""
# Open a file in read-write mode
fo = open("foo.txt", "w+")

# Write initial data to the file
fo.write("This is a rat race")

# Seek to a specific position in the file
fo.seek(10, 0)

# Read a few bytes from the current position
data = fo.read(3)
print("Data read from position 10:", data)

# Seek back to the same position
fo.seek(10, 0)

# Overwrite the earlier contents with new text
fo.write("cat")

# Rewind to the beginning of the file
fo.seek(0, 0)

# Read the entire file content
data = fo.read()
print("Updated file content:", data)

# Close the file
fo.close()
"""
Following is the output of the above code −

Data read from position 10: rat
Updated file content: This is a cat race
"""