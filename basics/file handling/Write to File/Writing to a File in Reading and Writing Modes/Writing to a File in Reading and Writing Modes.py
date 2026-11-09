"""
Writing to a File in Reading and Writing Modes
When a file is opened for writing using 'w' or 'a', it is not possible to perform write operations at any earlier byte position in the file. The 'w+' mode, however, allows both reading and writing operations without closing the file. The seek() function is used to move the read/write pointer to any desired byte position within the file.
"""