"""In Python, a warning is a message that indicates that something unexpected happened while running your code. Unlike an error, a warning will not stop the program from running. Warnings are used to alert the user about potential issues or deprecated features in the code.

For example, if you are using a deprecated module in your code, you will get a warning message saying that the module is deprecated and will be removed in future versions of Python. But your code may still work as expected.

Display a Warning Message
To display a warning message in Python, you can use the warn() function from the warnings module. Here is an example −
"""
import warnings

# Normal message
print("KeramatiAI")

# Warning message
warnings.warn("You got a warning!")
"""The output of the above code will be:

TutorialsPoint

Warnings/Errors:
/home/cg/root/d732ac89/main.py:7: UserWarning: You got a warning!
  warnings.warn("You got a warning!")"""