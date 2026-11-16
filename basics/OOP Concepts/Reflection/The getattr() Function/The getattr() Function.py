"""
The getattr() Function
The getattr() built-in function retrieves the value of the named attribute of object.

Example
"""
class test:
   def __init__(self):
      self.name = "Manav"

obj = test()
print (getattr(obj, "name"))
"""
It will produce the following output −

Manav
"""