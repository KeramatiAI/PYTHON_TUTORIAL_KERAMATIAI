"""
The callable() Function
An object is callable if it invokes a certain process. A Python function, which performs a certain process, is a callable object. Hence callable(function) returns True. Any function, built-in, user-defined, or method is callable. Objects of built-in data types such as int, str, etc., are not callable.

Example
"""
def test():
   pass

print (callable("Hello"))
print (callable(abs))
print (callable(list.clear([1,2])))
print (callable(test))
"""
A string object is not callable. But abs is a function which is callable. The pop method of list is callable, but clear() is actually call to the function and not a function object, hence not a callable

It will produce the following output −

False
True
True
False
True
A class instance is callable if it has a __call__() method. In the example below, the test class includes __call__() method. Hence, its object can be used as if we are calling function. Hence, object of a class with __call__() function is a callable.
"""
class test:
   def __init__(self):
      pass
   def __call__(self):
      print ("Hello")

obj = test()
obj()
print ("obj is callable?", callable(obj))
"""
It will produce the following output −

Hello
obj is callable? True
"""