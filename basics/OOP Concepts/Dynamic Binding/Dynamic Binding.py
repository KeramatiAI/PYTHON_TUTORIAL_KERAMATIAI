"""
In object-oriented programming, the concept of dynamic binding is closely related to polymorphism. In Python, dynamic binding is the process of resolving a method or attribute at runtime, instead of at compile time.

According to the polymorphism feature, different objects respond differently to the same method call based on their implementations. This behavior is achieved through method overriding, where a subclass provides its implementation of a method defined in its superclass.

The Python interpreter determines which is the appropriate method or attribute to invoke based on the object's type or class hierarchy at runtime. This means that the specific method or attribute to be called is determined dynamically, based on the actual type of the object.

Example
The following example illustrates dynamic binding in Python −
"""
class shape:
   def draw(self):
      print ("draw method")
      return

class circle(shape):
   def draw(self):
      print ("Draw a circle")
      return

class rectangle(shape):
   def draw(self):
      print ("Draw a rectangle")
      return

shapes = [circle(), rectangle()]
for shp in shapes:
   shp.draw()
"""
It will produce the following output −

Draw a circle
Draw a rectangle
As you can see, the draw() method is bound dynamically to the corresponding implementation based on the object's type. This is how dynamic binding is implemented in Python.
"""