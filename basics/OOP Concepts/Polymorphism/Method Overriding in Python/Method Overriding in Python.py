"""
Method Overriding in Python
In method overriding, a method defined inside a subclass has the same name as a method in its superclass but implements a different functionality.

Example
As an example of polymorphism given below, we have shape which is an abstract class. It is used as parent by two classes circle and rectangle. Both classes override parent's draw() method in different ways.
"""
from abc import ABC, abstractmethod
class shape(ABC):
   @abstractmethod
   def draw(self):
      "Abstract method"
      return

class circle(shape):
   def draw(self):
      super().draw()
      print ("Draw a circle")
      return

class rectangle(shape):
   def draw(self):
      super().draw()
      print ("Draw a rectangle")
      return

shapes = [circle(), rectangle()]
for shp in shapes:
   shp.draw()
Output
"""
When you run the above code, it will produce the following output −

Draw a circle
Draw a rectangle
"""