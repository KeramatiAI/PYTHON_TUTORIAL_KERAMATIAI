"""
Using append() method
To add a new element to an array, use the append() method. It accepts a single item as an argument and append it at the end of given array.

Syntax
Syntax of the append() method is as follows −

append(v)
Where,

v − new value is added at the end of the array. The new value must be of the same type as datatype argument used while declaring array object.

Example
Here, we are adding element at the end of specified array using append() method.
"""
import array as arr
a = arr.array('i', [1, 2, 3])
a.append(10)
print (a)
"""
It will produce the following output −

array('i', [1, 2, 3, 10])
"""