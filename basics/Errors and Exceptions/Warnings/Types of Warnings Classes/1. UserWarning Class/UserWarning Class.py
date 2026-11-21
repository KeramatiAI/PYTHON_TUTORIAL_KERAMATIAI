"""1. UserWarning Class
The UserWarning is the default warning class in Python. If you have any warning that does not fall into any of the other categories, it will be classified as a UserWarning. To specify a UserWarning, use UserWarning as the second argument to the warn() function. Here is an example −
"""
import warnings

# Warning message
warnings.warn("You got a warning!", UserWarning)
