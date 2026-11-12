"""
You can also assign default values to the formal arguments in the constructor so that the object can be instantiated with or without passing parameters.
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
"""