"""
Getters and Setter Methods
A getter method retrieves the value of an instance variable, usually named as get_varname, whereas the setter method assigns value to an instance variable − named as set_varname.

Example
Let us define getter methods get_name() and get_age(), and setters set_name() and set_age() in the Employee class.
"""
class Employee:
   def __init__(self, name, age):
      self.__name = name
      self.__age = age

   def get_name(self):
      return self.__name
   def get_age(self):
      return self.__age
   def set_name(self, name):
      self.__name = name
      return
   def set_age(self, age):
      self.__age=age

e1=Employee("Bhavana", 24)
print ("Name:", e1.get_name(), "age:", e1.get_age())
e1.set_name("Archana")
e1.set_age(21)
print ("Name:", e1.get_name(), "age:", e1.get_age())
"""
It will produce the following output −

Name: Bhavana age: 24
Name: Archana age: 21
The getter and setter methods can retrieve or assign value to instance variables. The property() function uses them to add property objects as class attributes.

The name property is defined as −

name = property(get_name, set_name, "name")
Similarly, you can add the age property −

age = property(get_age, set_age, "age")
The advantage of the property object is that you can use to retrieve the value of its associated instance variable, as well as assign value.

For example,

print (e1.name) displays value of e1.__name
e1.name = "Archana" assigns value to e1.__age

"""