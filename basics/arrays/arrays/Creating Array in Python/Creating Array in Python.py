"""
Creating Array in Python
To create an array in Python, import the array module and use its array() function. We can create an array of three basic types namely integer, float and Unicode characters using this function.

The array() function accepts typecode and initializer as a parameter value and returns an object of array class.

Syntax
The syntax for creating an array in Python is −

# importing
import array as array_name

# creating array
obj = array_name.array(typecode[, initializer])
Where,

typecode − The typecode character used to speccify the type of elements in the array.

initializer − It is an optional value from which array is initialized. It must be a list, a bytes-like object, or iterable elements of the appropriate type.

Example
The following example shows how to create an array in Python using the array module.
"""
import array as arr

# creating an array with integer type
a = arr.array('i', [1, 2, 3])
print (type(a), a)

# creating an array with char type
a = arr.array('u', 'BAT')
print (type(a), a)

# creating an array with float type
a = arr.array('d', [1.1, 2.2, 3.3])
print (type(a), a)
"""
It will produce the following output −

<class 'array.array'> array('i', [1, 2, 3])
<class 'array.array'> array('u', 'BAT')
<class 'array.array'> array('d', [1.1, 2.2, 3.3])
"""