"""
Using classmethod() Function
Python has a built-in function classmethod() which transforms an instance method to a class method which can be called with the reference to the class only and not the object.

Syntax
classmethod(instance_method)
Example
In the Employee class, define a showcount() instance method with the "self" argument (reference to calling object). It prints the value of empCount. Next, transform the method to class method counter() that can be accessed through the class reference.
"""
class Employee:
   empCount = 0
   def __init__(self, name, age):
      self.__name = name
      self.__age = age
      Employee.empCount += 1
   def showcount(self):
      print (self.empCount)

   counter = classmethod(showcount)

e1 = Employee("Bhavana", 24)
e2 = Employee("Rajesh", 26)
e3 = Employee("John", 27)

e1.showcount()
Employee.counter()
"""
Output
Call showcount() with object and call count() with class, both show the value of employee count.

3
3
"""