"""
Writing to a New File in Binary Mode
By default, read/write operations on a file object are performed on text string data. If we need to handle files of different types, such as media files (mp3), executables (exe), or pictures (jpg), we must open the file in binary mode by adding the 'b' prefix to the read/write mode.

Writing Binary Data to a File
To write binary data to a file, open the file in binary write mode ('wb'). The following example demonstrates this −
"""
# Open a file in binary write mode
with open('test.bin', 'wb') as f:
   # Binary data
   data = b"Hello World"
   f.write(data)

