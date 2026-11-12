"""
Using staticmethod() Function
Python's standard library function named staticmethod() is used to create a static method. It accepts a method as an argument and converts it into a static method.

Syntax
staticmethod(method)
Example
In the Employee class below, the showcount() method is converted into a static method. This static method can now be called by its object or reference of class itself.
"""
class Employee:
   empCount = 0
   def __init__(self, name, age):
      self.__name = name
      self.__age = age
      Employee.empCount += 1

   # creating staticmethod
   def showcount():
      print (Employee.empCount)
      return
   counter = staticmethod(showcount)

e1 = Employee("Bhavana", 24)
e2 = Employee("Rajesh", 26)
e3 = Employee("John", 27)

e1.counter()
Employee.counter()
"""
Executing the above code will print the following result −

3
3
"""