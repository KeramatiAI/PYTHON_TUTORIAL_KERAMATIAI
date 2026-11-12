"""
Parameterized Constructor
If a constructor is defined with multiple parameters along with self is called as parameterized constructor.

Example
In this example, the __init__() constructor has two formal arguments. We declare Employee objects with different values −
"""
class Employee:
   'Common base class for all employees'
   def __init__(self, name, age):
      self.name = name
      self.age = age

e1 = Employee("Bhavana", 24)
e2 = Employee("Bharat", 25)

print ("Name: {}".format(e1.name))
print ("age: {}".format(e1.age))
print ("Name: {}".format(e2.name))
print ("age: {}".format(e2.age))
"""
It will produce the following output −

Name: Bhavana
age: 24
Name: Bharat
age: 25
"""