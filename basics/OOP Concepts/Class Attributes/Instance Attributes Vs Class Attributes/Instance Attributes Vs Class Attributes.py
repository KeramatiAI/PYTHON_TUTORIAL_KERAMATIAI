"""
Instance Attributes Vs Class Attributes
The below table shows the difference between instance attributes and class attributes −

SNo.	Instance Attribute	Class Attribute
1	It is defined directly inside the __init__() function.	It is defined inside the class but outside the __init__() function.
2	Instance attribute is accessed using the object name followed by dot notation.	Class attributes can be accessed by both class name and object name.
3	The value of this attribute cannot be shared among other objects.	Its value is shared among other objects of the class.
4	Changes made to the instance attribute affect only the object within which it is defined.	Changes made to the class attribute affect all the objects of the given class.

"""