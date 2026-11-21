"""Example: Ignore Warnings
Here is a simple python code that shows how to ignore warnings −
"""
import warnings

# Ignore all warnings
warnings.filterwarnings("ignore")

print("Warning message: ")
warnings.warn("This warning will be ignored!")
"""The output of the above code will be:

Warning message: """