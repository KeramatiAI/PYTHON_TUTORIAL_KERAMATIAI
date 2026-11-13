"""
Hybrid Inheritance
Combination of two or more types of inheritance is called as Hybrid Inheritance. For instance, it could be a mix of single and multiple inheritance.

Example
In this example, we have combined single and multiple inheritance to form a hybrid inheritance of classes.
"""
# parent class
class CEO:
   def ceoMethod(self):
      print ("I am the CEO")

class Manager(CEO):
   def managerMethod(self):
      print ("I am the Manager")

class Employee1(Manager):
   def employee1Method(self):
      print ("I am Employee one")

class Employee2(Manager, CEO):
   def employee2Method(self):
      print ("I am Employee two")

# creating instances
emp = Employee2()
# method calls
emp.managerMethod()
emp.ceoMethod()
emp.employee2Method()
"""
On running the above program, it will give the below result −

I am the Manager
I am the CEO
I am Employee two
"""