"""
The super() function
In Python, super() function allows you to access methods and attributes of the parent class from within a child class.

Example
In the following example, we create a parent class and access its constructor from a subclass using the super() function.
"""
# parent class
class ParentDemo:
   def __init__(self, msg):
      self.message = msg

   def showMessage(self):
      print(self.message)

# child class
class ChildDemo(ParentDemo):
   def __init__(self, msg):
      # use of super function
      super().__init__(msg)

# creating instance
obj = ChildDemo("Welcome to KERAMATIAI!!")
obj.showMessage()
"""
On executing, the above program will give the following result −

Welcome to Tutorialspoint!!
"""