"""The raise . . from None Statement
If we use None in from clause instead of exception object, the automatic exception chaining that was found in the earlier example is disabled.
"""
try:
   open("nofile.txt")
except OSError as exc:
   raise RuntimeError from None
"""It will produce the following output −

Traceback (most recent call last):
 File "C:\Python311\hello.py", line 4, in <module>
  raise RuntimeError from None
RuntimeError"""