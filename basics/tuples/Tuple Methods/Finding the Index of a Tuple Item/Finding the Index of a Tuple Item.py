"""
The index() method of tuple class returns the index of first occurrence of the given item.

Syntax
tuple.index(obj)
Return value
The index() method returns an integer, representing the index of the first occurrence of "obj".
"""
tup1 = (25, 12, 10, -21, 10, 100)
print ("Tup1:", tup1)
x = tup1.index(10)
print ("First index of 10:", x)
"""
It will produce the following output −

Tup1: (25, 12, 10, -21, 10, 100)
First index of 10: 2
"""