"""
Python's built-in type() function returns the class that an object belongs to. In Python, a class, both a built-in class or a user-defined class are objects of type class.

Example
class myclass:
   def __init__(self):
      self.myvar=10
      return

obj = myclass()

print ('class of int', type(int))
print ('class of list', type(list))
print ('class of dict', type(dict))
print ('class of myclass', type(myclass))
print ('class of obj', type(obj))
It will produce the following output −

class of int <class 'type'>
class of list <class 'type'>
class of dict <class 'type'>
class of myclass <class 'type'>
The type() has a three argument version as follows −

Syntax
newclass=type(name, bases, dict)
Using above syntax, a class can be dynamically created. Three arguments of type function are −

name − name of the class which becomes __name__ attribute of new class

bases − tuple consisting of parent classes. Can be blank if not a derived class

dict − dictionary forming namespace of the new class containing attributes and methods and their values.
"""