"""
Inheritance
A software modelling approach of OOP enables extending capability of an existing class to build new class instead of building from scratch. In OOP terminology, existing class is called base or parent class, while new class is called child or sub class.

Child class inherits data definitions and methods from parent class. This facilitates reuse of features already available. Child class can add few more definitions or redefine a base class function.

Syntax
Derived classes are declared much like their parent class; however, a list of base classes to inherit from is given after the class name −

class SubClassName (ParentClass1[, ParentClass2, ...]):
   'Optional class documentation string'
   class_suite
Example
The following example demonstrates the concept of Inheritance in Python −
"""
#!/usr/bin/python
# define parent class
class Parent:
   parentAttr = 100
   def __init__(self):
      print ("Calling parent constructor")

   def parentMethod(self):
      print ("Calling parent method")

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print ("Parent attribute :", Parent.parentAttr)

# define child class
class Child(Parent):
   def __init__(self):
      print ("Calling child constructor")

   def childMethod(self):
      print ("Calling child method")

# instance of child
c = Child()
# child calls its method
c.childMethod()
# calls parent's method
c.parentMethod()
# again call parent's method
c.setAttr(200)
# again call parent's method
c.getAttr()
"""
When the above code is executed, it produces the following result −

Calling child constructor
Calling child method
Calling parent method
Parent attribute : 200
Similar way, you can drive a class from multiple parent classes as follows −

class A:        # define your class A
.....

class B:         # define your class B
.....

class C(A, B):   # subclass of A and B
.....
You can use issubclass() or isinstance() functions to check a relationships of two classes and instances.

The issubclass(sub, sup) boolean function returns true if the given subclass sub is indeed a subclass of the superclass sup.

The isinstance(obj, Class) boolean function returns true if obj is an instance of class Class or is an instance of a subclass of Class
"""