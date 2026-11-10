"""
Deleting Files in Python
You can delete a file in Python using the os.remove() function. This function deletes a file specified by its filename.

Syntax
Following is the basic syntax of the remove() function in Python −

os.remove(file_name)
Parameters
This function accepts the name of the file as a parameter which needs to be deleted.

Example
Following is an example to delete an existing file "file_to_delete.txt" using the remove() function −
"""
import os

# File to be deleted
file_to_delete = "file_to_delete.txt"

# Delete the file
os.remove(file_to_delete)

print(f"File '{file_to_delete}' deleted successfully.")
"""
After executing the above code, we get the following output −

File 'file_to_delete.txt' deleted successfully.
"""