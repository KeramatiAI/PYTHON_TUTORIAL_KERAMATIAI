"""
In software engineering, an interface is a software architectural pattern. It is similar to a class but its methods just have prototype signature definition without any executable code or implementation body. The required functionality must be implemented by the methods of any class that inherits the interface.

The method defined without any executable code is known as abstract method.
Interfaces in Python
In languages like Java and Go, there is keyword called interface which is used to define an interface. Python doesn't have it or any similar keyword. It uses abstract base classes (in short ABC module) and @abstractmethod decorator to create interfaces.

NOTE: In Python, abstract classes are also created using ABC module.

An abstract class and interface appear similar in Python. The only difference in two is that the abstract class may have some non-abstract methods, while all methods in interface must be abstract, and the implementing class must override all the abstract methods.

Rules for implementing Python Interfaces
We need to consider the following points while creating and implementing interfaces in Python −

Methods defined inside an interface must be abstract.
Creating object of an interface is not allowed.
A class implementing an interface needs to define all the methods of that interface.
In case, a class is not implementing all the methods defined inside the interface, the class must be declared abstract.
Ways to implement Interfaces in Python
We can create and implement interfaces in two ways −

Formal Interface
Informal Interface
"""