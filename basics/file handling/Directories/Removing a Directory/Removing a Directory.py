"""
Removing a Directory
You can remove an empty directory in Python using the os.rmdir() method. If the directory contains files or other directories, you can use shutil.rmtree() method to delete it recursively.

Syntax
Following is the basic syntax to delete a directory in Python −

os.rmdir(directory_path)
# or
shutil.rmtree(directory_path)
Example
In the following example, we remove an empty directory using the os.rmdir() method −
"""
import os
directory_path = r"D:\MyFolder\new_dir"

try:
   os.rmdir(directory_path)
   print(f"Directory '{directory_path}' successfully removed.")
except OSError as e:
   print(f"Error: Failed to remove directory '{directory_path}'. {e}")
"""
It will produce the following output −

Directory 'D:\MyFolder\new_dir' successfully removed.
"""