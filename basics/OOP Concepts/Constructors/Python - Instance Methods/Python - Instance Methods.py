"""
Python - Instance Methods
In addition to the __init__() constructor, there may be one or more instance methods defined in a class. A method with self as one of the formal arguments is called instance method, as it is called by a specific object.

Example
In the following example a displayEmployee() method has been defined as an instance method. It returns the name and age attributes of the Employee object that calls the method.
"""
class Employee:
   def __init__(self, name="Bhavana", age=24):
      self.name = name
      self.age = age
   def displayEmployee(self):
      print ("Name : ", self.name, ", age: ", self.age)

e1 = Employee()
e2 = Employee("Bharat", 25)

e1.displayEmployee()
e2.displayEmployee()
"""
It will produce the following output −

Name : Bhavana , age: 24
Name : Bharat , age: 25
You can add, remove, or modify attributes of classes and objects at any time −

# Add a 'salary' attribute
emp1.salary = 7000
# Modify 'name' attribute
emp1.name = 'xyz'
# Delete 'salary' attribute
del emp1.salary

Instead of using the normal statements to access attributes, you can use the following functions −

The getattr(obj, name[, default]) − to access the attribute of object.

The hasattr(obj,name) − to check if an attribute exists or not.

The setattr(obj,name,value) − to set an attribute. If attribute does not exist, then it would be created.

The delattr(obj, name) − to delete an attribute.

# Returns true if 'salary' attribute exists
print (hasattr(e1, 'salary'))
# Returns value of 'name' attribute
print (getattr(e1, 'name'))
# Set attribute 'salary' at 8
setattr(e1, 'salary', 7000) 
# Delete attribute 'age'
delattr(e1, 'age')

It will produce the following output −

False
Bhavana
"""