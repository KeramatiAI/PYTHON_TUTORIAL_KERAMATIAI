"""
Copy Arrays Using Assignment Operator
We can assign an array to another by using the assignment operator (=). However, such assignment doesn't create a new array in the memory. Instead, it creates a new reference to the same array.

Example
In the following example, we are using assignment operator to copy array in Python.
"""
import array as arr
a = arr.array('i', [110, 220, 330, 440, 550])
b = a
print("Copied array:",b)
print (id(a), id(b))
"""
It will produce the following output −

Copied array: array('i', [110, 220, 330, 440, 550])
134485392383792 134485392383792
Check the id() of both a and b. Same value of id confirms that simple assignment doesn't create a copy. Since "a" and "b" refer to the same array object, any change in the array "a" will reflect in "b" too −

a[2] = 10
print (a,b)
It will produce the following output −

array('i', [110, 220, 10, 440, 550]) array('i', [110, 220, 10, 440, 550])
"""