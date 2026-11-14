"""
Method Overriding in Python
The Python method overriding refers to defining a method in a subclass with the same name as a method in its superclass. In this case, the Python interpreter determines which method to call at runtime based on the actual object being referred to.

You can always override your parent class methods. One reason for overriding parent's methods is that you may want special or different functionality in your subclass.

Example
In the code below, we are overriding a method named myMethod of Parent class.
"""
# define parent class
class Parent:
   def myMethod(self):
      print ('Calling parent method')

# define child class
class Child(Parent):
   def myMethod(self):
      print ('Calling child method')

# instance of child
c = Child()
# child calls overridden method
c.myMethod()
"""
When the above code is executed, it produces the following output −

Calling child method
To understand Method Overriding in Python, let us take another example. We use following Employee class as parent class −
"""
class Employee:
   def __init__(self,nm, sal):
      self.name=nm
      self.salary=sal
   def getName(self):
      return self.name
   def getSalary(self):
      return self.salary
"""Next, we define a SalesOfficer class that uses Employee as parent class. It inherits the instance variables name and salary from the parent. Additionally, the child class has one more instance variable incentive.

We shall use built-in function super() that returns reference of the parent class and call the parent constructor within the child constructor __init__() method.
"""
class SalesOfficer(Employee):
   def __init__(self,nm, sal, inc):
      super().__init__(nm,sal)
      self.incnt=inc
   def getSalary(self):
      return self.salary+self.incnt
"""
(The getSalary() method is overridden to add the incentive to salary.)
"""