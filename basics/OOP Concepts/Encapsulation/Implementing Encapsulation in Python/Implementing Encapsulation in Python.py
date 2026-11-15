"""
Implementing Encapsulation in Python
Languages such as C++ and Java use access modifiers to restrict access to class members (i.e., variables and methods). These languages have keywords public, protected, and private to specify the type of access.

A class member is said to be public if it can be accessed from anywhere in the program. Private members are allowed to be accessed from within the class only. Usually, methods are defined as public, and instance variables are private. This arrangement of private instance variables and public methods ensures the implementation of encapsulation.

Unlike these languages, Python has no provision to specify the type of access that a class member may have. By default, all the variables and methods in a Python class are public, as demonstrated by the following example.

Example 1
Here, we have an Employee class with instance variables, name and age. An object of this class has these two attributes. They can be directly accessed from outside the class, because they are public.
"""
class Student:
   def __init__(self, name="Rajaram", marks=50):
      self.name = name
      self.marks = marks

s1 = Student()
s2 = Student("Bharat", 25)

print ("Name: {} marks: {}".format(s1.name, s2.marks))
print ("Name: {} marks: {}".format(s2.name, s2.marks))
"""
It will produce the following output −

Name: Rajaram marks: 50
Name: Bharat marks: 25
In the above example, the instance variables are initialized inside the class. However, there is no restriction on accessing the value of instance variables from outside the class, which is against the principle of encapsulation.

Although there are no keywords to enforce visibility, Python has a convention of naming the instance variables in a peculiar way. In Python, prefixing name of a variable/method with a single or double underscore to emulate the behavior of protected and private access modifiers.

If a variable is prefixed by a single double underscore (such as "__age"), the instance variable is private, similarly if a variable name is prefixed with a single underscore (such as "_salary")
"""