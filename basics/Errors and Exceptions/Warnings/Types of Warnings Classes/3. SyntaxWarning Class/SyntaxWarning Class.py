"""3. SyntaxWarning Class
The SyntaxWarning is used to indicate that there is a syntax-related issue in the code, but it is not severe enough to raise a SyntaxError. To specify a SyntaxWarning, use SyntaxWarning as the second argument to the warn() function. Here is an example −
"""
import warnings

# Warning message
warnings.warn("This is a syntax warning!", SyntaxWarning)

# Function with potential syntax issue
def func(x):
    return x is 10  # using "is" instead of "=="
