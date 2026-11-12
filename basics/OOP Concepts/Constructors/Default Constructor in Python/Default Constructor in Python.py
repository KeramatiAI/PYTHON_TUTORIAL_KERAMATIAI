"""
Default Constructor in Python
The Python constructor which does not accept any parameter other than self is called as default constructor.

Example
Let us define the constructor in the Employee class to initialize name and age as instance variables. We can then access these attributes through its object.
"""
class Employee:
   'Common base class for all employees'
   def __init__(self):
      self.name = "Bhavana"
      self.age = 24

e1 = Employee()
print ("Name: {}".format(e1.name))
print ("age: {}".format(e1.age))
"""
It will produce the following output −

Name: Bhavana
age: 24
For the above Employee class, each object we declare will have same value for its instance variables name and age. To declare objects with varying attributes instead of the default, define arguments for the __init__() method.
"""