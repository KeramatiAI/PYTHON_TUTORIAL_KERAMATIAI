"""
Using + operator
We can also use + operator to concatenate or merge two arrays. In this approach, we first convert arrays to list objects, then concatenate the lists using the + operator and convert back to get merged array.

Example: Join Two Arrays by Converting to List Objects
In this example, we will see how to join two arrays using + operator.
"""
import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
b = arr.array('i', [2,7,8,11,3,10])
x = a.tolist()
y = b.tolist()
z = x+y
a = arr.array('i', z)
print (a)
"""
The above code will display the following output −

array('i', [10, 5, 15, 4, 6, 20, 9, 2, 7, 8, 11, 3, 10])
"""