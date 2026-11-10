"""
Get Current Working Directory
To retrieve the current working directory in Python, you can use the os.getcwd() function. This function returns a string representing the current working directory where the Python script is executing.

Syntax
Following is the basic syntax of the getcwd() function in Python −

os.getcwd()
Example
Following is an example to display the current working directory using the getcwd() function −
"""
import os

current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")
"""
We get the output as follows −

Current working directory: /home/cg/root/667ba7570a5b7
"""