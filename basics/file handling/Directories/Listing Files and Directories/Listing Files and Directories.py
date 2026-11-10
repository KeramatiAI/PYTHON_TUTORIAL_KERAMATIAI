"""
Listing Files and Directories
You can list the contents of a directory using the os.listdir() function. This function returns a list of all files and directories within the specified directory path.

Example
In the example below, we are listing the contents of the specified directory path using the listdir() function −
"""
import os

directory_path = r"D:\MyFolder\Pictures"

try:
   contents = os.listdir(directory_path)
   print(f"Contents of '{directory_path}':")
   for item in contents:
      print(item)
except OSError as e:
   print(f"Error: Failed to list contents of directory '{directory_path}'. {e}")
"""
Output of the above code is as shown below −

Contents of 'D:\MyFolder\Pictures':
Camera Roll
desktop.ini
Saved Pictures
Screenshots
"""