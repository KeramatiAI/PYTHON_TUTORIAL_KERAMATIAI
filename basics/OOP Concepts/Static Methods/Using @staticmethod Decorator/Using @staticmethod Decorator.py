"""
Using @staticmethod Decorator
The second way to create a static method is by using the Python @staticmethod decorator. When we use this decorator with a method it indicates to the Interpreter that the specified method is static.

Syntax
@staticmethod
def method_name():
   # your code
Example
In the following example, we are creating a static method using the @staticmethod decorator.
"""
class Student:
   stdCount = 0
   def __init__(self, name, age):
      self.__name = name
      self.__age = age
      Student.stdCount += 1

   # creating staticmethod
   @staticmethod
   def showcount():
      print (Student.stdCount)

e1 = Student("Bhavana", 24)
e2 = Student("Rajesh", 26)
e3 = Student("John", 27)

print("Number of Students:")
Student.showcount()
"""
Running the above code will print the following result −

Number of Students:
3
"""