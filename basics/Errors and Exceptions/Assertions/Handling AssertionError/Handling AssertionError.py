"""Handling AssertionError
Assertions can be caught and handled like any other exception using a try-except block. If they are not handled, they will terminate the program and produce a traceback −
"""
try:
   num = int(input('Enter a number: '))
   assert num >= 0, "Only non-negative numbers are accepted"
   print(num)
except AssertionError as msg:
   print(msg)
"""It will produce the following output −

Enter a number: -87
Only non-negative numbers are accepted"""