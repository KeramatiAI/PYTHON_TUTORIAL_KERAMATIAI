"""
Using enumerate() function
The enumerate() function can be used to access elements of an array. It accepts an array and an optional starting index as parameter values and returns the array items by iterating.

Example
In the below example, we will see how to use the enumerate() function to access array items.
"""
import array as arr

# creating array
numericArray = arr.array('i', [111, 211, 311, 411, 511])

# use of enumerate() function
for loc, val in enumerate(numericArray):
    print(f"Index: {loc}, value: {val}")
"""
It will produce the following output −

Index: 0, value: 111
Index: 1, value: 211
Index: 2, value: 311
Index: 3, value: 411
Index: 4, value: 511
"""