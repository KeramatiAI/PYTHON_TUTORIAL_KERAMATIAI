"""
Method Resolution Order (MRO)
The term method resolution order is related to multiple inheritance in Python. In Python, inheritance may be spread over more than one levels. Let us say A is the parent of B, and B the parent for C. The class C can override the inherited method or its object may invoke it as defined in its parent. So, how does Python find the appropriate method to call.

Each Python has a mro() method that returns the hierarchical order that Python uses to resolve the method to be called. The resolution order is from bottom of inheritance order to top.

In our previous example, the div_mod class inherits division and modulus classes. So, the mro method returns the order as follows −

[<class '__main__.div_mod'>, <class '__main__.division'>, <class '__main__.modulus'>, <class 'object'>]
Python - Multilevel Inheritance
In multilevel inheritance, a class is derived from another derived class. There exists multiple layers of inheritance. We can imagine it as a grandparent-parent-child relationship.

Example
In the following example, we are illustrating the working of multilevel inheritance.
"""
# parent class
class Universe:
   def universeMethod(self):
      print ("I am in the Universe")

# child class
class Earth(Universe):
   def earthMethod(self):
      print ("I am on Earth")

# another child class
class India(Earth):
   def indianMethod(self):
      print ("I am in India")

# creating instance
person = India()
# method calls
person.universeMethod()
person.earthMethod()
person.indianMethod()
"""
When we execute the above code, it will produce the following result −

I am in the Universe
I am on Earth
I am in India
"""