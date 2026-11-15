"""
Abstract Method Overriding
Hence, the child class with the abstract method overridden is given in the following example −

Example
"""
from abc import ABC, abstractmethod
class democlass(ABC):
   @abstractmethod
   def method1(self):
      print ("abstract method")
      return
   def method2(self):
      print ("concrete method")

class concreteclass(democlass):
   def method1(self):
      super().method1()
      return

obj = concreteclass()
obj.method1()
obj.method2()
"""
Output
When you execute this code, it will produce the following output −

abstract method
concrete method
"""