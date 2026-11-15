"""
Encapsulation is the process of bundling attributes and methods within a single unit. It is one of the main pillars on which the object-oriented programming paradigm is based.

We know that a class is a user-defined prototype for an object. It defines a set of data members and methods, capable of processing the data.

According to the principle of data encapsulation, the data members that describe an object are hidden from the environment external to the class. They can only be accessed through the methods within the same class. Methods themselves on the other hand are accessible from outside class context. Hence, object data is said to be encapsulated by the methods. In this way, encapsulation prevents direct access to the object data.

Implementing Encapsulation in Python
Languages such as C++ and Java use access modifiers to restrict access to class members (i.e., variables and methods). These languages have keywords public, protected, and private to specify the type of access.

A class member is said to be public if it can be accessed from anywhere in the program. Private members are allowed to be accessed from within the class only. Usually, methods are defined as public, and instance variables are private. This arrangement of private instance variables and public methods ensures the implementation of encapsulation.

Unlike these languages, Python has no provision to specify the type of access that a class member may have. By default, all the variables and methods in a Python class are public, as demonstrated by the following example.
"""