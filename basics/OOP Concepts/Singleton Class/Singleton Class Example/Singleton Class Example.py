"""
Example
In the below example, we are creating a singleton class using the __init__ method.
"""
class Singleton:
  __uniqueInstance = None

  @staticmethod
  def createInstance():
    if Singleton.__uniqueInstance == None:
      Singleton()
    return Singleton.__uniqueInstance

  def __init__(self):
      if Singleton.__uniqueInstance != None:
          raise Exception("Object exist!")
      else:
          Singleton.__uniqueInstance = self

obj1 = Singleton.createInstance()
print(obj1)
obj2 = Singleton.createInstance()
print(obj2)
"""
When we run the above code, it will show the following result −

<__main__.Singleton object at 0x7e4da068a910>
<__main__.Singleton object at 0x7e4da068a910>
"""