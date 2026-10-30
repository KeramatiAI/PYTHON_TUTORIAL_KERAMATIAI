"""
The count() method in tuple class returns the number of times a given object occurs in the tuple.

Syntax
tuple.count(obj)
Return Value
Number of occurrence of the object. The count() method returns an integer.
"""
tup1 = (10, 20, 45, 10, 30, 10, 55)
print ("Tup1:", tup1)
c = tup1.count(10)
print ("count of 10:", c)
"""
It will produce the following output −

Tup1: (10, 20, 45, 10, 30, 10, 55)
count of 10: 3
"""