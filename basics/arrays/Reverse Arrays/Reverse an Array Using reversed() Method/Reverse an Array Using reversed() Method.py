"""
Reverse an Array Using reversed() Method
The reversed() method is another way to reverse elements of an array. It accepts an array as a parameter value and returns an iterator object that dispalys array elements in reverse order.

Example
In this example, we are using the reversed() method to reverse an array in Python.
"""
import array as arr

# creating an array
numericArray = arr.array('i', [12, 10, 14, 16, 20, 18])
print("Array before reversing:", numericArray)

# reversing the array
newArray = list(reversed(numericArray))

# creating a new array from reversed list
revArray = arr.array('i', newArray)
print ("Array after reversing:",revArray)
"""
On executing the above code, it will display the following output −

Array before reversing: array('i', [12, 10, 14, 16, 20, 18])
Array after reversing: array('i', [18, 20, 16, 14, 10, 12])
"""