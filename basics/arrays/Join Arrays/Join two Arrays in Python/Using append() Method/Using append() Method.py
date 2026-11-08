"""
Using append() Method
To join two arrays, we can append each item from one array to other using append() method. To perform this operation, run a for loop on the original array, fetch each element and append it to a new array.

Example: Join Two Arrays by Appending Elements
Here, we use the append() method to join two arrays.
"""
import array as arr

# creating two arrays
a = arr.array('i', [10,5,15,4,6,20,9])
b = arr.array('i', [2,7,8,11,3,10])

# merging both arrays
for i in range(len(b)):
   a.append(b[i])
print (a)
"""
It will produce the following output −

array('i', [10, 5, 15, 4, 6, 20, 9, 2, 7, 8, 11, 3, 10])
"""