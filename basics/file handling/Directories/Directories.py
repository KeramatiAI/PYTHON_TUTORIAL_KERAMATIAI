"""
Directories in Python
In Python, directories, commonly known as folders in operating systems, are locations on the filesystem used to store files and other directories. They serve as a way to group and manage files hierarchically.

Python provides several modules, primarily os and os.path, along with shutil, that allows you to perform various operations on directories.

These operations include creating new directories, navigating through existing directories, listing directory contents, changing the current working directory, and removing directories.

Checking if a Directory Exists
Before performing operations on a directory, you often need to check if it exists. We can check if a directory exists or not using the os.path.exists() function in Python.

This function accepts a single argument, which is a string representing a path in the filesystem. This argument can be −

Relative path − A path relative to the current working directory.

Absolute path − A complete path starting from the root directory.

Example
In this example, we check whether the given directory path exists using the os.path.exists() function −
"""
import os

directory_path = "D:\\Test\\MyFolder\\"

if os.path.exists(directory_path):
   print(f"The directory '{directory_path}' exists.")
else:
   print(f"The directory '{directory_path}' does not exist.")
"""
Following is the output of the above code −

The directory 'D:\\Test\\MyFolder\\' exists.
"""