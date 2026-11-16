"""
Multilevel Inner Class
It refers to an inner class that itself contains another inner class. It creates multiple levels of nested classes.

Example
The following code explains the working of Multilevel Inner Class in Python −
"""
class Organization:
   def __init__(self):
      self.inner = self.Department()

   def showName(self):
      print("Organization Name: Tutorials Point")

   class Department:
      def __init__(self):
         self.innerTeam = self.Team1()

      def displayDep(self):
         print("In Department")

      class Team1:
         def displayTeam(self):
            print("Team 1 of the department")

# instance of outer class
outer = Organization()
# call the method of outer class
outer.showName()

# Inner Class instance
inner = outer.inner
inner.displayDep()

# Access Team1 instance
innerTeam = inner.innerTeam
# Calling display method
innerTeam.displayTeam()
"""
When you run the above code, it will produce the below output −

Organization Name: Tutorials Point
In Department
Team 1 of the department
"""