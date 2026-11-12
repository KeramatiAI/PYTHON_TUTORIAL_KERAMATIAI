"""Example
The complete program with property objects and their use is given below −"""

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
      return
   name = property(get_name, set_name, "name")
   age = property(get_age, set_age, "age")

e1=Employee("Bhavana", 24)
print ("Name:", e1.name, "age:", e1.age)

e1.name = "Archana"
e1.age = 23
print ("Name:", e1.name, "age:", e1.age)
"""It will produce the following output −

Name: Bhavana age: 24
Name: Archana age: 23"""