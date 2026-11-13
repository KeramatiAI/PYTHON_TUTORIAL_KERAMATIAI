"""
Single Inheritance
This is the simplest form of inheritance where a child class inherits attributes and methods from only one parent class.

Example
The below example shows single inheritance concept in Python −
"""
# parent class
class Parent:
   def parentMethod(self):
      print ("Calling parent method")

# child class
class Child(Parent):
   def childMethod(self):
      print ("Calling child method")

# instance of child
c = Child()
# calling method of child class
c.childMethod()
# calling method of parent class
c.parentMethod()
"""
On running the above code, it will print the following result −

Calling child method
Calling parent method
"""