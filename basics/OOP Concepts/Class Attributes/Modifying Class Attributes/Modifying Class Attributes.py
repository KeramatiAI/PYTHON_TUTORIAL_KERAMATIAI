"""
Modifying Class Attributes
To modify the value of a class attribute, we simply need to assign a new value to it using the class name followed by dot notation and attribute name.

Example
In the below example, we are initializing a class variable called empCount in Employee class. For each object declared, the __init__() method is automatically called. This method initializes the instance variables as well as increments the empCount by 1.
"""
class Employee:
   # class attribute
   empCount = 0
   def __init__(self, name, age):
      self.__name = name
      self.__age = age
      # modifying class attribute
      Employee.empCount += 1
      print ("Name:", self.__name, ", Age: ", self.__age)
      # accessing class attribute
      print ("Employee Count:", Employee.empCount)

e1 = Employee("Bhavana", 24)
print()
e2 = Employee("Rajesh", 26)
"""
Output
We have declared two objects. Every time, the empCount increments by 1.

Name: Bhavana , Age:  24
Employee Count: 1

Name: Rajesh , Age:  26
Employee Count: 2
"""