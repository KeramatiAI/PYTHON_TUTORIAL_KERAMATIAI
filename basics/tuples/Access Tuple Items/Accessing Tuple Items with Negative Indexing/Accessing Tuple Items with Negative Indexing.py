"""
Accessing Tuple Items with Negative Indexing
Negative indexing in Python is used to access elements from the end of a tuple, with -1 referring to the last element, -2 to the second last, and so on.

We can also access tuple items with negative indexing by using negative integers to represent positions from the end of the tuple.

Example
In the following example, we are accessing tuple items with negative indexing −
"""
tup1 = ("a", "b", "c", "d")
tup2 = (25.50, True, -55, 1+2j)

print ("Item at 0th index in tup1: ", tup1[-1])
print ("Item at index 2 in tup2: ", tup2[-3])
"""
We get the output as shown below −

Item at 0th index in tup1:  d
Item at index 2 in tup2:  True
"""