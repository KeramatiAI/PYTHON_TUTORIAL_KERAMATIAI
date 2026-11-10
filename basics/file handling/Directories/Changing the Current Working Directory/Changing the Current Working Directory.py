"""
Changing the Current Working Directory
You can change the current directory using the chdir() method. This method takes an argument, which is the name of the directory that you want to make the current directory.

Syntax
Following is the syntax of the chdir() method in Python −

os.chdir("newdir")
Example
Following is an example to change the current directory to Desktop using the chdir() method −
"""
import os

new_directory = r"D:\MyFolder\Pictures"

try:
    os.chdir(new_directory)
    print(f"Current working directory changed to '{new_directory}'.")
except OSError as e:
    print(f"Error: Failed to change working directory to '{new_directory}'. {e}")
"""
We get the output as shown below −

Current working directory changed to 'D:\MyFolder\Pictures'.
"""