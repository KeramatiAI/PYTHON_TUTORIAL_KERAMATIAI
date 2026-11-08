"""
Using extend() Method
Another approach to concatenate arrays is the use of extend() method from the List class. Similar to above approach, we first convert the array to a list and then call the extend() method to merge the two lists.

Example: Join Two Arrays using extend() Method
In the following example, we will use the extend() method to concatenate two arrays in Python.
"""
import array as arr
a = arr.array('i', [88, 99, 77, 66, 44, 22])
b = arr.array('i', [12, 17, 18, 11, 13, 10])
a.extend(b)
print (a)
"""
It will produce the following output −

array('i', [88, 99, 77, 66, 44, 22, 12, 17, 18, 11, 13, 10])
"""