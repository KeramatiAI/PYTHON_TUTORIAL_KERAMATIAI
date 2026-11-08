"""
Python for Loop with Array Index
We can find the length of array with built-in len() function. Use it to create a range object to get the series of indices and then access the array elements in a for loop.

Example
The code below illustrates how to use for loop with array index.
"""
import array as arr
a = arr.array('d', [56, 42, 23, 85, 45])
l = len(a)
for x in range(l):
   print (a[x])
"""
On running the above code, it will show the below output −

56.0
42.0
23.0
85.0
45.0
"""