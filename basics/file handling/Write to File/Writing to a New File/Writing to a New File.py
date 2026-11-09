"""
Writing to a New File
Writing to a new file in Python involves creating a new file (or overwriting an existing one) and writing the desired content to it. Here, we will explain the steps involved in writing to a new file −

Open the File − Use the open() function to create or open a file in write mode ("w" or "wb" for binary files).

Write Data − Use the write() or writelines() method to write data to the file.

Close the File − Ensure the file is properly closed after writing, generally using the "with" statement for automatic handling.

Example
In the example below, we create a "foo.txt" file and write given content in that file and finally close that file −
"""
# Open a file
fo = open("foo.txt", "w")
fo.write( "Python is a great language.\nYeah its great!!\n")

# Close opened file
fo.close()
"""
If you open this file with any text editor application such as Notepad, it will have the following content −

Python is a great language.
Yeah its great!!
"""