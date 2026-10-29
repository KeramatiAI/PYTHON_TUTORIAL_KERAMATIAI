"""
The Python extend() function is used to append elements from an iterable (such as another list) to the end of the list. This function modifies the original list in place, adding the elements of the iterable to the end of the list.

The extend() function is not used for joining tuples in Python. It is used to extend a list by appending elements from another iterable (such as another list), effectively merging the two lists together.
We can join tuples using the extend() function by temporarily converting the tuples into lists, performing the joining operation as if they were lists, and then converting the resulting list back into a tuple.
"""
T1 = (10,20,30,40)
T2 = ('one', 'two', 'three', 'four')
L1 = list(T1)
L2 = list(T2)
L1.extend(L2)
T1 = tuple(L1)
print ("Joined Tuple:", T1)