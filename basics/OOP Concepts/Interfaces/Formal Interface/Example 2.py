"""
Let us provide a class that implements both the abstract methods.
"""
# class implementing the above interface
class concreteclass(demoInterface):
   def method1(self):
      print ("This is method1")
      return

   def method2(self):
      print ("This is method2")
      return

# creating instance
obj = concreteclass()

# method call
obj.method1()
obj.method2()
"""
Output
When you execute this code, it will produce the following output −

This is method1
This is method2
"""