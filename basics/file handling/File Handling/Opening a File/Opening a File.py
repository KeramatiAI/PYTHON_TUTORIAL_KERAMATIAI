"""
Opening a File in Python
To perform any file operation, the first step is to open the file. Python's built-in open() function is used to open files in various modes, such as reading, writing, and appending. The syntax for opening a file in Python is −

file = open("filename", "mode")
Where, filename is the name of the file to open and mode is the mode in which the file is opened (e.g., 'r' for reading, 'w' for writing, 'a' for appending).

File Opening Modes
Following are the file opening modes −

Sr.No.	Modes & Description
1
r

Opens a file for reading only. The file pointer is placed at the beginning of the file. This is the default mode.

2
rb

Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file. This is the default mode.

3
r+

Opens a file for both reading and writing. The file pointer placed at the beginning of the file.

4
rb+

Opens a file for both reading and writing in binary format. The file pointer placed at the beginning of the file.

5
w

Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.

6
b

Opens the file in binary mode

7
t

Opens the file in text mode (default)

8
+

open file for updating (reading and writing)

9
wb

Opens a file for writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.

10
w+

Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.

11
wb+

Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.

12
a

Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.

13
ab

Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.

14
a+

Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.

15
ab+

Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.

16
x

open for exclusive creation, failing if the file already exists

Once a file is opened and you have one file object, you can get various information related to that file.
"""
"""
Example 1
In the following example, we are opening a file in different modes −
"""
# Opening a file in read mode
file = open("example.txt", "r")

# Opening a file in write mode
file = open("example.txt", "w")

# Opening a file in append mode
file = open("example.txt", "a")

# Opening a file in binary read mode
file = open("example.txt", "rb")

