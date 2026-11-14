"""
Duck Typing
Another concept closely related to dynamic binding is duck typing. Whether an object is suitable for a particular use is determined by the presence of certain methods or attributes, rather than its type. This allows for greater flexibility and code reuse in Python.

Duck typing is an important feature of dynamic typing languages like Python (Perl, Ruby, PHP, Javascript, etc.) that focuses on an object's behavior rather than its specific type. According to the "duck typing" concept, "If it walks like a duck and quacks like a duck, then it must be a duck."

Duck typing allows objects of different types to be used interchangeably as long as they have the required methods or attributes. The goal is to promote flexibility and code reuse. It is a broader concept that emphasizes object behavior and interface rather than formal types.

Here is an example of duck typing −
"""
class circle:
   def draw(self):
      print ("Draw a circle")
      return

class rectangle:
   def draw(self):
      print ("Draw a rectangle")
      return

class area:
   def area(self):
      print ("calculate area")
      return

def duck_function(obj):
   obj.draw()

objects = [circle(), rectangle(), area()]
for obj in objects:
   duck_function(obj)
"""
It will produce the following output −

Draw a circle
Draw a rectangle
Traceback (most recent call last):
 File "C:\Python311\hello.py", line 21, in <module>
  duck_function(obj)
 File "C:\Python311\hello.py", line 17, in duck_function
 obj.draw()
AttributeError: 'area' object has no attribute 'draw'
The most important idea behind duck typing is that the duck_function() doesn't care about the specific types of objects it receives. It only requires the objects to have a draw() method. If an object "quacks like a duck" by having the necessary behavior, it is treated as a "duck" for the purpose of invoking the draw() method.

Thus, in duck typing, the focus is on the object's behavior rather than its explicit type, allowing different types of objects to be used interchangeably as long as they exhibit the required behavior.
"""