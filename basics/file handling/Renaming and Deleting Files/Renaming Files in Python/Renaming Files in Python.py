"""
Renaming Files in Python
To rename a file in Python, you can use the os.rename() function. This function takes two arguments: the current filename and the new filename.

Syntax
Following is the basic syntax of the rename() function in Python −

os.rename(current_file_name, new_file_name)
Parameters
Following are the parameters accepted by this function −

current_file_name − It is the current name of the file you want to rename.

new_file_name − It is the new name you want to assign to the file.

Example
Following is an example to rename an existing file "oldfile.txt" to "newfile.txt" using the rename() function −
"""
import os

# Current file name
current_name = "oldfile.txt"

# New file name
new_name = "newfile.txt"

# Rename the file
os.rename(current_name, new_name)

print(f"File '{current_name}' renamed to '{new_name}' successfully.")
"""
Following is the output of the above code −

File 'oldfile.txt' renamed to 'newfile.txt' successfully.
"""