"""5. ImportWarning Class
The ImportWarning is used to indicate that there is an issue related to the import of a module. To specify an ImportWarning, use ImportWarning as the second argument to the warn() function. Here is an example −
"""
import warnings

# Warning message
warnings.warn("This is an import warning!", ImportWarning)
