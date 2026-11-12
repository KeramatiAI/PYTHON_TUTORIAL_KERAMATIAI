"""
Access Built-In Class Attributes
To access built-in class attributes in Python, we use the class name followed by a dot (.) and then attribute name.

Example
For the Employee class, we are trying to access all the built-in class attributes −
"""
class Employee:
   def __init__(self, name="Bhavana", age=24):
      self.name = name
      self.age = age
   def displayEmployee(self):
      print ("Name : ", self.name, ", age: ", self.age)

print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__ )
"""
Output
It will produce the following output −

Employee.__doc__: None
Employee.__name__: Employee
Employee.__module__: __main__
Employee.__bases__: (<class 'object'>,)
Employee.__dict__: {'__module__': '__main__', '__init__': <function Employee.__init__ at 0x0000022F866B8B80>, 'displayEmployee': <function Employee.displayEmployee at 0x0000022F866B9760>, '__dict__': <attribute '__dict__' of 'Employee' objects>, '__weakref__': <attribute '__weakref__' of 'Employee' objects>, '__doc__': None}
"""