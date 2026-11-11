"""
Accessing Attributes of Objects in Python
You access the object's attributes using the dot operator with object. Class variable would be accessed using class name as follows −

emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)
Now, putting all the concepts together −
"""


class Employee:
    "Common base class for all employees"
    empCount = 0

    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


# This would create first object of Employee class
emp1 = Employee("Zara", 2000,55)
# This would create second object of Employee class
emp2 = Employee("Manni", 5000,36)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)
"""
When the above code is executed, it produces the following result −

Name :  Zara , Salary:  2000
Name :  Manni , Salary:  5000
Total Employee 2
"""

"""
You can add, remove, or modify attributes of classes and objects at any time −
"""
# Add an 'age' attribute
emp1.age = 7
# Modify 'age' attribute
emp1.age = 8
# Delete 'age' attribute
del emp1.age
"""
Instead of using the normal statements to access attributes, you can also use the following functions −

getattr(obj, name[, default]) − to access the attribute of object.

hasattr(obj,name) − to check if an attribute exists or not.

setattr(obj,name,value) − to set an attribute. If attribute does not exist, then it would be created.

delattr(obj, name) − to delete an attribute.
"""
# Returns true if 'age' attribute exists
hasattr(emp1, 'age')
# Returns value of 'age' attribute
getattr(emp1, 'age')
# Set attribute 'age' at 8
setattr(emp1, 'age', 8)
# Delete attribute 'age'
delattr(emp1, 'age')
# Delete attribute 'age'
delattr(emp1, 'age')
