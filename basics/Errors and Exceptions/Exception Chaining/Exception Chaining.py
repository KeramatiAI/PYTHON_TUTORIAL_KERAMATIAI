"""Exception Chaining
Exception chaining is a technique of handling exceptions by re-throwing a caught exception after wrapping it inside a new exception. The original exception is saved as a property (such as cause) of the new exception.

During the handling of one exception 'A', it is possible that another exception 'B' may occur. It is useful to know about both exceptions in order to debug the problem. Sometimes it is useful for an exception handler to deliberately re-raise an exception, either to provide extra information or to translate an exception to another type.

In Python 3.x, it is possible to implement exception chaining. If there is any unhandled exception inside an except section, it will have the exception being handled attached to it and included in the error message.

Example
In the following code snippet, trying to open a non-existent file raises FileNotFoundError. It is detected by the except block. While handling another exception is raised.
"""
try:
   open("nofile.txt")
except OSError:
   raise RuntimeError("unable to handle error")
"""It will produce the following output −

Traceback (most recent call last):
  File "/home/cg/root/64afcad39c651/main.py", line 2, in <module>
open("nofile.txt")
FileNotFoundError: [Errno 2] No such file or directory: 'nofile.txt'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/cg/root/64afcad39c651/main.py", line 4, in <module>
    raise RuntimeError("unable to handle error")
RuntimeError: unable to handle error"""