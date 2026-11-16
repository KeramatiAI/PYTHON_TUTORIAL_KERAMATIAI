"""
Anonymous Class and Object Example
We can also add instance variables and instance methods dynamically. Take a look at this example −
"""
def getA(self):
   return self.a
obj = type('',(object,),{'a':5,'b':6,'c':7,'getA':getA,'getB':lambda self : self.b})()
print (obj.getA(), obj.getB())
"""
It will produce the following output −

5 6
"""