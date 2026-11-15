"""
Formal Interface
Formal interfaces in Python are implemented using abstract base class (ABC). To use this class, you need to import it from the abc module.

Example
In this example, we are creating a formal interface with two abstract methods.
"""
from abc import ABC, abstractmethod

# creating interface
class demoInterface(ABC):
   @abstractmethod
   def method1(self):
      print ("Abstract method1")
      return

   @abstractmethod
   def method2(self):
      print ("Abstract method1")
      return

