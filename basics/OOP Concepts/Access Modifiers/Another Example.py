"""
Let us modify the Employee class. Add another instance variable salary. Make age private and salary as protected by prefixing double and single underscores respectively.
"""
class Employee:
   def __init__(self, name, age, salary):
      self.name = name # public variable
      self.__age = age # private variable
      self._salary = salary # protected variable
   def displayEmployee(self):
      print ("Name : ", self.name, ", age: ", self.__age, ", salary: ", self._salary)

e1=Employee("Bhavana", 24, 10000)

print (e1.name)
print (e1._salary)
print (e1.__age)
"""
When you run this code, it will produce the following output −

Bhavana
10000
Traceback (most recent call last):
 File "C:\Users\user\example.py", line 14, in <module>
  print (e1.__age)
        ^^^^^^^^
AttributeError: 'Employee' object has no attribute '__age'
Python displays AttributeError because __age is private, and not available for use outside the class.
"""