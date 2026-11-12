"""
Name Mangling
Python doesn't block access to private data, it just leaves for the wisdom of the programmer, not to write any code that access it from outside the class. You can still access the private members by Python's name mangling technique.

Name mangling is the process of changing name of a member with double underscore to the form object._class__variable. If so required, it can still be accessed from outside the class, but the practice should be refrained.

In our example, the private instance variable "__name" is mangled by changing it to the format −

obj._class__privatevar
So, to access the value of "__age" instance variable of "e1" object, change it to "e1._Employee__age".

Change the print() statement in the above program to −

print (e1._Employee__age)
It now prints 24, the age of e1.

Python Property Object
Python's standard library has a built-in property() function. It returns a property object. It acts as an interface to the instance variables of a Python class.

The encapsulation principle of object-oriented programming requires that the instance variables should have a restricted private access. Python doesn't have efficient mechanism for the purpose. The property() function provides an alternative.

The property() function uses the getter, setter and delete methods defined in a class to define a property object for the class.

Syntax
property(fget=None, fset=None, fdel=None, doc=None)
Parameters
fget − an instance method that retrieves value of an instance variable.

fset − an instance method that assigns value to an instance variable.

fdel − an instance method that removes an instance variable

fdoc − Documentation string for the property.

The function uses getter and setter methods to return the property object.
"""