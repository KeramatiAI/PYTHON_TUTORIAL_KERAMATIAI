"""
Accessing a range of array items in Python
In Python, to access a range of array items, you can use the slicing operation which is performed using index operator [] and colon (:).

This operation is implemented using multiple formats, which are listed below −

Use the [:index] format to access elements from beginning to desired range.

To access array items from end, use [:-index] format.

Use the [index:] format to access array items from specific index number till the end.

Use the [start index : end index] to slice the array elements within a range. You can also pass an optional argument after end index to determine the increment between each index.

Example
The following example demonstrates the slicing operation in Python.
"""
import array as arr

# creating array
numericArray = arr.array('i', [111, 211, 311, 411, 511])

# slicing operation
print (numericArray[2:])
print (numericArray[0:3])
"""
On executing the above code, it will display the following result −

array('i', [311, 411, 511])
array('i', [111, 211, 311])
"""