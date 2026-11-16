"""
The isinstance() Function
This is another built-in function in Python which ascertains if an object is an instance of the given class.

Syntax
isinstance(obj, class)
This function always returns a Boolean value, true if the object is indeed belongs to the given class and false if not.

Example
Following statements return True −
"""
print (isinstance(10, int))
print (isinstance(2.56, float))
print (isinstance(2+3j, complex))
print (isinstance("Hello World", str))
"""
It will produce the following output −

True
True
True
True
In contrast, these statements print False.
"""
print (isinstance([1,2,3], tuple))
print (isinstance({1:'one', 2:'two'}, set))
"""
It will produce the following output −

False
False
You can also perform check with a user defined class
"""
class test:
   pass

obj = test()
print (isinstance(obj, test))
"""
It will produce the following output −

True
In Python, even the classes are objects. All classes are objects of object class. It can be verified by following code −
"""
class test:
   pass

print (isinstance(int, object))
print (isinstance(str, object))
print (isinstance(test, object))
"""
All the above print statements print True.
"""