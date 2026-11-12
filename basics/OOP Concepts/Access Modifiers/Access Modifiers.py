"""
The Python access modifiers are used to restrict access to class members (i.e., variables and methods) from outside the class. There are three types of access modifiers namely public, protected, and private.

Public members − A class member is said to be public if it can be accessed from anywhere in the program.

Protected members − They are accessible from within the class as well as by classes derived from that class.

Private members − They can be accessed from within the class only.

Usually, methods are defined as public and instance variable are private. This arrangement of private instance variables and public methods ensures implementation of principle of encapsulation.

Access Modifiers in Python
Unlike C++ and Java, Python does not use the Public, Protected and Private keywords to specify the type of access modifiers. By default, all the variables and methods in a Python class are public.

Example
Here, we have Employee class with instance variables name and age. An object of this class has these two attributes. They can be directly accessed from outside the class, because they are public.
"""
class Employee:
   'Common base class for all employees'
   def __init__(self, name="Bhavana", age=24):
      self.name = name
      self.age = age

e1 = Employee()
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
Python doesn't enforce restrictions on accessing any instance variable or method. However, Python prescribes a convention of prefixing name of variable/method with single or double underscore to emulate behavior of protected and private access modifiers.

To indicate that an instance variable is private, prefix it with double underscore (such as "__age").
To imply that a certain instance variable is protected, prefix it with single underscore (such as "_salary").
"""