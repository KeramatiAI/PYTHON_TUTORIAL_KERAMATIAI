"""
What is Name Mangling?
Python doesn't block access to private data entirely. It just leaves it to the wisdom of the programmer, not to write any code that accesses it from outside the class. You can still access the private members by Python's name mangling technique.

Name mangling is the process of changing name of a member with double underscore to the form object._class__variable. If so required, it can still be accessed from outside the class, but the practice should be refrained.

In our example, the private instance variable "__name" is mangled by changing it to the format

obj._class__privatevar
So, to access the value of "__marks" instance variable of "s1" object, change it to "s1._Student__marks".

Change the print() statement in the above program to −

print (s1._Student__marks)
It now prints 50, the marks of s1.

Hence, we can conclude that Python doesn't implement encapsulation exactly as per the theory of object-oriented programming. It adapts a more mature approach towards it by prescribing a name convention and letting the programmer use name mangling if it is really required to have access to private data in the public scope.
"""