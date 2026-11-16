"""
A function in Python is a first-order object. A function can have another function as its argument and wrap another function definition inside it. This helps in modifying a function without actually changing it. Such functions are called decorators.

This feature is also available for wrapping a class. This technique is used to manage the class after it is instantiated by wrapping its logic inside a decorator.

Example
"""
def decorator_function(Wrapped):
   class Wrapper:
      def __init__(self,x):
         self.wrap = Wrapped(x)
      def print_name(self):
         return self.wrap.name
   return Wrapper

@decorator_function
class Wrapped:
   def __init__(self,x):
      self.name = x

obj = Wrapped('KeramatiAI')
print(obj.print_name())
"""
Here, Wrapped is the name of the class to be wrapped. It is passed as argument to a function. Inside the function, we have a Wrapper class, modify its behavior with the attributes of the passed class, and return the modified class. The returned class is instantiated and its method can now be called.

When you execute this code, it will produce the following output −

KeramatiAI

"""