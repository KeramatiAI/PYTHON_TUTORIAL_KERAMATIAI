"""
Creating a Directory
You create a new directory in Python using the os.makedirs() function. This function creates intermediate directories if they do not exist.

The os.makedirs() function accepts a "path" you want to create as an argument. It optionally accepts a "mode" argument that specifies the permissions o set for the newly created directories. It is an integer, represented in octal format (e.g., 0o755). If not specified, the default permissions are used based on your system's umask.

Example
In the following example, we are creating a new directory using the os.makedirs() function −
"""
import os

new_directory = "new_dir.txt"

try:
   os.makedirs(new_directory)
   print(f"Directory '{new_directory}' created successfully.")
except OSError as e:
   print(f"Error: Failed to create directory '{new_directory}'. {e}")
"""
After executing the above code, we get the following output −

Directory 'new_dir.txt' created successfully.
The mkdir() Method
You can use the mkdir() method of the os module to create directories in the current directory. You need to supply an argument to this method, which contains the name of the directory to be created.

Following is the syntax of the mkdir() method in Python −

os.mkdir("newdir")
Example
Following is an example to create a directory test in the current directory −
"""
import os

# Create a directory "test"
os.mkdir("test")
print ("Directory created successfully")
"""
The result obtained is as shown below −

Directory created successfully
"""