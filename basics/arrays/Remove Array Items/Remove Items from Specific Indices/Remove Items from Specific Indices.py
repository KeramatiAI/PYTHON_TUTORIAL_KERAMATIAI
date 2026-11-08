"""
Remove Items from Specific Indices
To remove an array element from specific index, use the pop() method. This method removes an element at the specified index from the array and returns the element at ith position after removal.

Syntax
array.pop(i)
Where, i is the index for the element to be removed.

Example
In this example, we will see how to use pop() method to remove elements from an array.
"""
import array as arr

# creating array
numericArray = arr.array('i', [111, 211, 311, 411, 511])

# before removing array
print ("Before removing:", numericArray)
# removing array
numericArray.pop(3)
# after removing array
print ("After removing:", numericArray)
"""
It will produce the following output −

Before removing: array('i', [111, 211, 311, 411, 511])
After removing: array('i', [111, 211, 311, 511])
"""