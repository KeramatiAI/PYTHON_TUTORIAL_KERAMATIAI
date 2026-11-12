"""
Dynamically Delete Class Methods
The Python del operator is used to delete a class method dynamically. If you try to access the deleted method, the code will raise AttributeError.

Example
In the below example, we are deleting the class method named "brandName" using del operator.
"""
class Cloth:
   # class method
   @classmethod
   def brandName(cls):
      print("Name of the brand is Raymond")

# deleting dynamically
del Cloth.brandName
print("Method deleted")
"""
On executing the above code, it will show the following output −

Method deleted
"""