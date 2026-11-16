"""
The issubclass() Function
This function checks whether a class is a subclass of another class. Pertains to classes, not their instances.

As mentioned earlier, all Python classes are subclassed from object class. Hence, output of following print statements is True for all.
"""
class test:
   pass

print (issubclass(int, object))
print (issubclass(str, object))
print (issubclass(test, object))
"""
It will produce the following output −

True
True
True
"""