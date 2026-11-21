"""Warning Filters
Warning filters are used to control the behavior of warning messages in Python. For example, if you feel that a warning is severe, you can convert it into an error so that program will stop running. Or, if you feel that a warning is not important, you can ignore it.

The filterwarnings() function from the warnings module can be used to specify warning filters. It can take following parameters:

default − This is the default behavior. It displays the first occurrence of each warning for each location where the warning is issued.
always − This option will always display the warning message, even if it has been displayed before.
ignore − This option is used to prevent the display of warning messages.
error − This option converts the warning into an exception, which will stop the program from running.
module − This option will print the first occurrence of matching warnings for each module where the warning is issued.
once − This option will print the first occurrence of matching warnings, regardless of the location.
Example: Turn Warning to an Error
Here is a simple python code that shows how to turn warnings into errors −
"""
import warnings

# Turn warning into an error
warnings.filterwarnings("error", category=UserWarning)
try:
    warnings.warn("This is a warning!", UserWarning)
except UserWarning as e:
    print("Caught as error:", e)
"""The output of the above code will be −

Caught as error: This is a warning!"""