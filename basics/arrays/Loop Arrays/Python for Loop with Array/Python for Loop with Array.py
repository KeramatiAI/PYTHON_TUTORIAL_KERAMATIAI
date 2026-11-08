"""
Python for Loop with Array
The for loop is used when the number of iterations is known. If we use it with an iterable like array, the iteration continues until it has iterated over every element in the array.

Example
The below example demonstrates how to iterate over an array using the "for" loop −
"""
import array as arr
newArray = arr.array('i', [56, 42, 23, 85, 45])
for iterate in newArray:
   print (iterate)
"""
The above code will produce the following result −

56
42
23
85
45
"""