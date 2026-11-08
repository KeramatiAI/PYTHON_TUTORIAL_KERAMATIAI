"""
Using slicing operation
Slicing operation is the process of extracting a part of array within the specified indices. In Python, if we use the slice operation in the form [::-1] then, it will display a new array by reversing the original one.

In this process, the interpreter starts from the end and stepping backwards by 1 until it reaches the beginning of the array. As a result, we get a reverse copy of original array.

Example
The below example demonstrates how to use the slicing operation to reverse an array in Python.
"""
import array as arr

# creating array
numericArray = arr.array('i', [88, 99, 77, 55, 66])

print("Original array:", numericArray)
revArray = numericArray[::-1]
print("Reversed array:",revArray)
"""
When you run the code, it will produce the following output −

Original array: array('i', [88, 99, 77, 55, 66])
Reversed array: array('i', [66, 55, 77, 99, 88])
"""