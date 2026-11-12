"""
Instance Attributes
As stated earlier, an instance attribute in Python is a variable that is specific to an individual object of a class. It is defined inside the __init__() method.

The first parameter of this method is self and using this parameter the instance attributes are defined.

Example
In the following code, we are illustrating the working of instance attributes.
"""
class Student:
   def __init__(self, name, grade):
      self.__name = name
      self.__grade = grade
      print ("Name:", self.__name, ", Grade:", self.__grade)

# Creating instances
student1 = Student("Ram", "B")
student2 = Student("Shyam", "C")
"""
Output
On running the above code, it will produce the following output −

Name: Ram , Grade: B
Name: Shyam , Grade: C
"""