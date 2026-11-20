"""The __context__ and __cause__ Expression
Raising an exception in the except block will automatically add the captured exception to the __context__ attribute of the new exception. Similarly, you can also add __cause__ to any exception using the expression raise ... from syntax.
"""
try:
   try:
      raise ValueError("ValueError")
   except ValueError as e1:
      raise TypeError("TypeError") from e1
except TypeError as e2:
   print("The exception was", repr(e2))
   print("Its __context__ was", repr(e2.__context__))
   print("Its __cause__ was", repr(e2.__cause__))
"""It will produce the following output −

The exception was TypeError('TypeError')
Its __context__ was ValueError('ValueError')
Its __cause__ was ValueError('ValueError')"""