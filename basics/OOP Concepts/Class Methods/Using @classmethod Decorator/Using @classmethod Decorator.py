"""
Using @classmethod Decorator
Use of @classmethod() decorator is the prescribed way to define a class method as it is more convenient than first declaring an instance method and then transforming it into a class method.

Syntax
@classmethod
def method_name():
   # your code
Example
The class method acts as an alternate constructor. Define a newemployee() class method with arguments required to construct a new object. It returns the constructed object, something that the __init__() method does.
"""
class Employee:
    empCount = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Employee.empCount += 1

    @classmethod
    def showcount(cls):
        print (cls.empCount)

    @classmethod
    def newemployee(cls, name, age):
        return cls(name, age)

e1 = Employee("Bhavana", 24)
e2 = Employee("Rajesh", 26)
e3 = Employee("John", 27)
e4 = Employee.newemployee("Anil", 21)

Employee.showcount()
"""
There are four Employee objects now. If we run the above program, it will show the count of Employee object −

4
"""