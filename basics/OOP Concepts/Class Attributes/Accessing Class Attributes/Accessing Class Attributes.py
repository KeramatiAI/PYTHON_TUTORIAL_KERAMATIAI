"""
Accessing Class Attributes
The object name followed by dot notation (.) is used to access class attributes.

Example
The below example demonstrates how to access the attributes of a Python class.
"""
class Employee:
   name = "Bhavesh Aggarwal"
   age = "30"

# instance of the class
emp = Employee()
# accessing class attributes
print("Name of the Employee:", emp.name)
print("Age of the Employee:", emp.age)
"""
Output
Name of the Employee: Bhavesh Aggarwal
Age of the Employee: 30
"""