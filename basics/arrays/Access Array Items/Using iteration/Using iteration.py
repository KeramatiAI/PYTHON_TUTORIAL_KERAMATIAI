"""
Using iteration
In this approach, a block of code is executed repeatedely using loops such as for and while. It is used when you want to access array elements one by one.

Example
In the below code, we use the for loop to access all the elements of the specified array.
"""
import array as arr

# creating array
numericArray = arr.array('i', [111, 211, 311, 411, 511])

# iteration through for loop
for item in numericArray:
   print(item)
"""
On executing the above code, it will display the following result −

111
211
311
411
511
"""