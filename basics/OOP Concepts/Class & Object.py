"""
Class & Object
A class is an user-defined prototype for an object that defines a set of attributes that characterize any object of the class. The attributes are data members (class variables and instance variables) and methods, accessed via dot notation.

An object refers to an instance of a certain class. For example, an object named obj that belongs to a class Circle is an instance of that class. A unique instance of a data structure that is defined by its class. An object comprises both data members (class variables and instance variables) and methods.

Example
The below example illustrates how to create a class and its object in Python.
"""
# defining class
class Smartphone:
   # constructor
   def __init__(self, device, brand):
      self.device = device
      self.brand = brand

   # method of the class
   def description(self):
      return f"{self.device} of {self.brand} supports Android 14"

# creating object of the class
phoneObj = Smartphone("Smartphone", "Samsung")
print(phoneObj.description())
"""
On executing the above code, it will display the following output −

Smartphone of Samsung supports Android 14
"""