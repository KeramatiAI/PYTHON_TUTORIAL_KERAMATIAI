"""
Dynamically Add Class Method to a Class
The Python setattr() function is used to set an attribute dynamically. If you want to add a class method to a class, pass the method name as a parameter value to setattr() function.

Example
The following example shows how to add a class method dynamically to a Python class.
"""
class Cloth:
   pass

# class method
@classmethod
def brandName(cls):
   print("Name of the brand is Raymond")

# adding dynamically
setattr(Cloth, "brand_name", brandName)
newObj = Cloth()
newObj.brand_name()
"""
When we execute the above code, it will show the following output −

Name of the brand is Raymond
"""