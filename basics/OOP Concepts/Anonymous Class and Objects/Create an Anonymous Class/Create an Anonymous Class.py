"""
Create an Anonymous Class
We can create an anonymous class with the above version of type() function. The name argument is a null string, second argument is a tuple of one class the object class (note that each class in Python is inherited from object class). We add certain instance variables as the third argument dictionary. We keep it empty for now.

anon=type('', (object, ), {})

"""
anon=type('', (object, ), {})