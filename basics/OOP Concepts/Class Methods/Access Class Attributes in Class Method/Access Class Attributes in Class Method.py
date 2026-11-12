"""
Access Class Attributes in Class Method
Class attributes are those variables that belong to a class and whose value is shared among all the instances of that class.

To access class attributes within a class method, use the cls parameter followed by dot (.) notation and name of the attribute.

Example
In this example, we are accessing a class attribute in class method.
"""
class Cloth:
   # Class attribute
   price = 4000

   @classmethod
   def showPrice(cls):
      return cls.price

# Accessing class attribute
print(Cloth.showPrice())
"""
On running the above code, it will show the following output −

4000
"""