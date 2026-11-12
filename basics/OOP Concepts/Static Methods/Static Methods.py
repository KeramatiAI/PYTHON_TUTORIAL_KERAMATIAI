"""
What is Python Static Method?
In Python, a static method is a type of method that does not require any instance to be called. It is very similar to the class method but the difference is that the static method doesn't have a mandatory argument like reference to the object − self or reference to the class − cls.

Static methods are used to access static fields of a given class. They cannot modify the state of a class since they are bound to the class, not instance.

How to Create Static Method in Python?
There are two ways to create Python static methods −

Using staticmethod() Function
Using @staticmethod Decorator
"""