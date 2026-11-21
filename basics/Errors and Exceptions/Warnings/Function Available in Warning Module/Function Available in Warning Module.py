"""
Function Available in Warning Module
The warnings module has couple of functions that you can use to manage warnings in your Python code. Here are some of the most commonly used functions −

1. warnings.warn()
This function is used to issue a warning message. You can specify the warning message and the category of the warning. The syntax of the function is −

warnings.warn(message, category=None, stacklevel=1,
              source=None, *, skip_file_prefixes=())
Here, message is the warning message you want to display, and category is the type of warning (e.g., UserWarning, DeprecationWarning, etc.).

The stacklevel argument can be used by wrapper functions written in Python to adjust the stack level of the warning. The skip_file_prefixes keyword argument can be used to indicate which stack frames are ignored when counting stack levels.

2. warnings.showwarning()
The showwarning() function is used to write warning messages to a file. Here is the syntax of the function:

warnings.showwarning(message, category, filename, lineno, file=None, line=None)
Here, message is the warning message, category is the type of warning, filename is the name of the file where the warning should be saved, lineno is the line number where the warning occurred.

3. warnings.warn_explicit()
The warn_explicit() function is used to send a warning message with more control over the warning's context. It can be used to explicitly pass the message, category, filename and line number, and optionally the module name and the registry. Here is the syntax of the function −

warnings.warn_explicit(message, category, filename, lineno, module=None,
                        registry=None, module_globals=None, source=None)
The parameters have same meaning as in the previous functions.

4. warnings.filterwarnings()
The filterwarnings() function is used to set the warning filters. we have already disscussed how to use this function to ignore, always display, or convert warnings into errors. Here is the proper syntax of the function −

warnings.filterwarnings(action, message='', category=Warning, module='', lineno=0, append=False)
The parameter "action" can take any of the following values: "default", "always", "ignore", "error", "module", or "once". The other parameters are optional.

5. warnings.simplefilter()
The simplefilter() function is a simpler interface to the filterwarnings() function. It is used to set a filter for a specific category of warnings. Here is the syntax of the function −

warnings.simplefilter(action, category=Warning, lineno=0, append=False)
The parameters have same meaning as in the previous functions.

6. warnings.resetwarnings()
The resetwarnings() function is used to reset the warning filters to their default state. This can be useful if you want to clear any custom warning filters you have set. Here is the syntax of the function −

warnings.resetwarnings()
This function does not take any parameters.

Conclusion
In this chapter, we learned about warnings in Python. Warnings are different from errors because they will not stop the program from running. It is just used to alert the programmer about potential issues in the code. The warnings module provides a way to issue warning messages and control their behavior.
"""