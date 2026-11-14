"""
Example
The below example shows how to achieve method overloading in Python −
"""
class example:
   def add(self, a = None, b = None, c = None):
      x=0
      if a !=None and b != None and c != None:
         x = a+b+c
      elif a !=None and b != None and c == None:
         x = a+b
      return x

obj = example()

print (obj.add(10,20,30))
print (obj.add(10,20))
"""
It will produce the following output −

60
30
With this workaround, we are able to incorporate method overloading in Python class.
"""