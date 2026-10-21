"""
Arbitrary Arguments (*args)
You may want to define a function that is able to accept arbitrary or variable number of arguments. Moreover, the arbitrary number of arguments might be positional or keyword arguments.

An argument prefixed with a single asterisk * for arbitrary positional arguments.

An argument prefixed with two asterisks ** for arbitrary keyword arguments.
"""
"""
Arbitrary Arguments Example
Given below is an example of arbitrary or variable length positional arguments −
"""
# sum of numbers
def add(*args):
   s=0
   for x in args:
      s=s+x
   return s
result = add(10,20,30,40)
print (result)

result = add(1,2,3)
print (result)

result = add(100,200,350,8000,657,214000,87000000,980000000,999999999999999999999999999999999)
print (result)