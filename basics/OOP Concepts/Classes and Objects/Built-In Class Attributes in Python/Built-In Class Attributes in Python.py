"""
Built-In Class Attributes in Python
Every Python class keeps following built-in attributes and they can be accessed using dot operator like any other attribute −

SNo.	Attributes & Description
1	__dict__
Dictionary containing the class's namespace.

2	__doc__
Class documentation string or none, if undefined.

3	__name__
Class name

4	__module__
Module name in which the class is defined. This attribute is "__main__" in interactive mode.

5	__bases__
A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.

Example
For the above Employee class, let us try to access its attributes −
"""
class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1

   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__)
"""When the above code is executed, it produces the following result −

Employee.__doc__: Common base class for all employees
Employee.__name__: Employee
Employee.__module__: __main__
Employee.__bases__: ()
Employee.__dict__: {'__module__': '__main__', 'displayCount':
<function displayCount at 0xb7c84994>, 'empCount': 2, 
'displayEmployee': <function displayEmployee at 0xb7c8441c>, 
'__doc__': 'Common base class for all employees', 
'__init__': <function __init__ at 0xb7c846bc>}
"""