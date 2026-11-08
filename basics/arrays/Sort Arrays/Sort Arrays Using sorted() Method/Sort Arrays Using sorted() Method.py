"""
Sort Arrays Using sorted() Method
The third technique to sort an array is with the sorted() function, which is a built-in function.

The syntax of sorted() function is as follows −

sorted(iterable, reverse=False)
The function returns a new list containing all items from the iterable in ascending order. Set reverse parameter to True to get a descending order of items.

The sorted() function can be used along with any iterable. Python array is an iterable as it is an indexed collection. Hence, an array can be used as a parameter to sorted() function.

Example
In this example, we will see the use of sorted() method in sorting an array.
"""
import array as arr
a = arr.array('i', [4, 5, 6, 9, 10, 15, 20])
sorted(a)
print(a)
"""
It will produce the following output −

array('i', [4, 5, 6, 9, 10, 15, 20])
"""