"""
Using __new__
The __new__ method is a special static method in Python that is called to create a new instance of a class. It takes the class itself as the first argument and returns a new instance of that class.

When an instance of a Python class is declared, it internally calls the __new__() method. If you want to implement a Singleton class, you can override this method.

In the overridden method, you first check whether an instance of the class already exists. If it doesnt (i.e., if the instance is None), you call the super() method to create a new object. At the end, save this instance in a class attribute and return the result.

Example
In the following example, we are creating a singleton class using the __new__ method.
"""
class SingletonClass:
   _instance = None

   def __new__(cls):
      if cls._instance is None:
         print('Creating the object')
         cls._instance = super(SingletonClass, cls).__new__(cls)
      return cls._instance

obj1 = SingletonClass()
print(obj1)

obj2 = SingletonClass()
print(obj2)
"""
The above code gives the following result −

Creating the object
<__main__.SingletonClass object at 0x000002A5293A6B50>
<__main__.SingletonClass object at 0x000002A5293A6B50>
"""