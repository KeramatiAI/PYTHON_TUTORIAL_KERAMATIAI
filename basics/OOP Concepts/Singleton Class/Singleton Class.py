"""
In Python, a Singleton class is the implementation of singleton design pattern which means this type of class can have only one object. This helps in optimizing memory usage when you perform some heavy operation, like creating a database connection.

If we try to create multiple objects for a singleton class, the object will be created only for the first time. After that, the same object instance will be returned.

Creating Singleton Classes in Python
We can create and implement singleton classes in Python using the following ways −

using __init__
using __new__
Using __init__
The __init__ method is an instance method that is used for initializing a newly created object. Its automatically called when an object is created from a class.

If we use this method with a static method and provide necessary checks i.e., whether an instance of the class already exists or not, we can restrict the creation of a new object after the first one is created.
"""