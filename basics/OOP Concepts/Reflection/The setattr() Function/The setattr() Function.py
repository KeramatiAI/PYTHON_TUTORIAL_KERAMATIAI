"""
The setattr() Function
The setattr() built-in function adds a new attribute to the object and assigns it a value. It can also change the value of an existing attribute.

In the example below, the object of test class has a single attribute − name. We use setattr() to add age attribute and to modify the value of name attribute.
"""
class test:
   def __init__(self):
      self.name = "Manav"

obj = test()
setattr(obj, "age", 20)
setattr(obj, "name", "Madhav")
print (obj.name, obj.age)
"""
It will produce the following output −

Madhav 20
"""