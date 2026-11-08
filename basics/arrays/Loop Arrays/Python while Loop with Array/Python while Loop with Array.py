"""
Python while Loop with Array
In while loop, the iteration continues as long as the specified condition is true. When you are using this loop with arrays, initialize a loop variable before entering the loop. This variable often represents an index for accessing elements in the array. Inside the while loop, iterate over the array elements and manually update the loop variable.

Example
The following example shows how you can loop through an array using a while loop −
"""
import array as arr

# creating array
a = arr.array('i', [96, 26, 56, 76, 46])

# checking the length
l = len(a)

# loop variable
idx = 0

# while loop
while idx < l:
   print (a[idx])
   # incrementing the while loop
   idx+=1
"""
On executing the above code, it will display the following output −

96
26
56
76
46
"""