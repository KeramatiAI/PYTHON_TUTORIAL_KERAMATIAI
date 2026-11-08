"""
Remove First Occurrence
To remove the first occurrence of a given value from the array, use remove() method. This method accepts an element and removes it if the element is available in the array.

Syntax
array.remove(v)
Where, v is the value to be removed from the array.

Example
The below example shows the usage of remove() method. Here, we are removing an element from the specified array.
"""
import array as arr

# creating array
numericArray = arr.array('i', [111, 211, 311, 411, 511])

# before removing array
print ("Before removing:", numericArray)
# removing array
numericArray.remove(311)
# after removing array
print ("After removing:", numericArray)
"""
It will produce the following output −

Before removing: array('i', [111, 211, 311, 411, 511])
After removing: array('i', [111, 211, 411, 511])
"""