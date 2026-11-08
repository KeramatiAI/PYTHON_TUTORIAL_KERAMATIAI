"""
Using for Loop
To reverse an array using a for loop, we first traverse the elements of the original array in reverse order and then append each element to a new array.

Example
The following example shows how to reverse an array in Python using for loop.
"""
import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
b = arr.array('i')
for i in range(len(a)-1, -1, -1):
   b.append(a[i])
print(a)
print(b)
"""
It will produce the following output −

array('i', [10, 5, 15, 4, 6, 20, 9])
array('i', [9, 20, 6, 4, 15, 5, 10])
"""