"""
Reading a File in Binary Mode
By default, read/write operation on a file object are performed on text string data. If we want to handle files of different types, such as media files (mp3), executables (exe), or pictures (jpg), we must open the file in binary mode by adding the 'b' prefix to the read/write mode.

Writing to a Binary File
Assuming that the test.bin file has already been written in binary mode −
"""
# Open the file in binary write mode
with open('test.bin', 'wb') as f:
   data = b"Hello World"
   f.write(data)
"""
Example
To read a binary file, we need to open it in 'rb' mode. The returned value of the read() method is then decoded before printing −
"""
# Open the file in binary read mode
with open('test.bin', 'rb') as f:
   data = f.read()
   print(data.decode(encoding='utf-8'))
"""
It will produce the following output −

Hello World
"""