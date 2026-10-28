"""
Accessing Range of Tuple Items with Negative Indexing
By range of tuple items, we mean accessing a subset of elements from a tuple using slicing. Therefore, we can access a range of tuple items with negative indexing by using the slicing operation in Python.

Example
In the example below, we are accessing a range of tuple items by using negative indexing −
"""
tup1 = ("a", "b", "c", "d")
tup2 = (1, 2, 3, 4, 5)

print ("Items from index 1 to last in tup1: ", tup1[1:])
print ("Items from index 2 to last in tup2", tup2[2:-1])
"""
It will produce the following output −

Items from index 1 to last in tup1: ('b', 'c', 'd')
Items from index 2 to last in tup2: (3, 4)
"""
