"""The raise . . from Statement
If you use an optional from clause in the raise statement, it indicates that an exception is a direct consequence of another. This can be useful when you are transforming exceptions. The token after from keyword should be the exception object.
"""
try:
   open("nofile.txt")
except OSError as exc:
   raise RuntimeError from exc
"""It will produce the following output −

Traceback (most recent call last):
  File "/home/cg/root/64afcad39c651/main.py", line 2, in <module>
    open("nofile.txt")
FileNotFoundError: [Errno 2] No such file or directory: 'nofile.txt'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/cg/root/64afcad39c651/main.py", line 4, in <module>
    raise RuntimeError from exc
RuntimeError"""