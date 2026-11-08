"""
Using insert() method
It is possible to add a new element at the specified index using the insert() method. The array module in Python defines this method. It accepts two parameters which are index and value and returns a new array after adding the specified value.

Syntax
Syntax of this method is shown below −

insert(i, v)
Where,

i − The index at which new value is to be inserted.

v − The value to be inserted. Must be of the arraytype.

Example
The following example shows how to add array elements at specific index with the help of insert() method.
"""
import array as arr
a = arr.array('i', [1, 2, 3])
a.insert(1,20)
print (a)
"""
It will produce the following output −

array('i', [1, 20, 2, 3])
"""