"""
The hasattr() Function
This built-in function returns True if the given attribute is available to the object argument, and false if not. We use the same test class and check if it has a certain attribute or not.
"""
class test:
   def __init__(self):
      self.name = "Manav"

obj = test()
print (hasattr(obj, "age"))
print (hasattr(obj, "name"))
"""
It will produce the following output −

False
True
"""