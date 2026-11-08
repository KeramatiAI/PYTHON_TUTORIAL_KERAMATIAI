"""
Using extend() method
The extend() method belongs to Python array module. It is used to add all elements from an iterable or array of same data type.

Syntax
This method has the following syntax −

extend(x)
Where,

x − This parameter specifies an array or iterable.

Example
In this example, we are adding items from another array to the specified array.
"""
import array as arr
a = arr.array('i', [1, 2, 3, 4, 5])
b = arr.array('i', [6,7,8,9,10])
a.extend(b)
print (a)
"""
On executing the above code, it will produce the following output −

array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
"""