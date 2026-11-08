"""
Reverse an Array Using reverse() Method
We can also reverse the sequence of numbers in an array using the reverse() method of list class. Here, list is a built-in type in Python.

Since reverse() is a method of list class, we cannot directly use it to reverse an array created through the Python array module. We have to first transfer the contents of an array to a list with tolist() method of array class, then we call the reverse() method and at the end, when we convert the list back to an array, we get the array with reversed order.

Example
Here, we will see the use of reverse() method in reversing an array in Python.
"""
import array as arr

# creating an array
numericArray = arr.array('i', [10,5,15,4,6,20,9])
print("Array before reversing:", numericArray)

# converting the array into list
newArray = numericArray.tolist()

# reversing the list
newArray.reverse()

# creating a new array from reversed list
revArray = arr.array('i', newArray)
print ("Array after reversing:",revArray)
"""
It will produce the following output −

Array before reversing: array('i', [10, 5, 15, 4, 6, 20, 9])
Array after reversing: array('i', [9, 20, 6, 4, 15, 5, 10])
"""