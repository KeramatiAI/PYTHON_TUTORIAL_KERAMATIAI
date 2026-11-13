"""
What is Inheritance in Python?
Inheritance is one of the most important features of object-oriented programming languages like Python. It is used to inherit the properties and behaviours of one class to another. The class that inherits another class is called a child class and the class that gets inherited is called a base class or parent class.

If you have to design a new class whose most of the attributes are already well defined in an existing class, then why redefine them? Inheritance allows capabilities of existing class to be reused and if required extended to design a new class.

Inheritance comes into picture when a new class possesses 'IS A' relationship with an existing class. For example, Car IS a vehicle, Bus IS a vehicle, Bike IS also a vehicle. Here, Vehicle is the parent class, whereas car, bus and bike are the child classes.

inheritance
Creating a Parent Class
The class whose attributes and methods are inherited is called as parent class. It is defined just like other classes i.e. using the class keyword.

Syntax
The syntax for creating a parent class is shown below −

class ParentClassName:
   {class body}
Creating a Child Class
Classes that inherit from base classes are declared similarly to their parent class, however, we need to provide the name of parent classes within the parentheses.

Syntax
Following is the syntax of child class −

class SubClassName (ParentClass1[, ParentClass2, ...]):
   {sub class body}
Types of Inheritance
In Python, inheritance can be divided in five different categories −

Single Inheritance
Multiple Inheritance
Multilevel Inheritance
Hierarchical Inheritance
Hybrid Inheritance
types of inheritance
"""