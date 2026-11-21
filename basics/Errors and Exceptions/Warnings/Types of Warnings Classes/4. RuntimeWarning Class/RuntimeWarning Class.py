"""4. RuntimeWarning Class
The RuntimeWarning is a base class used to indicate that there is a doubtful issue related to runtime. To specify a RuntimeWarning, use RuntimeWarning as the second argument to the warn() function. Here is an example −
"""
import warnings

# Warning message
warnings.warn("This is a runtime warning!", RuntimeWarning)
