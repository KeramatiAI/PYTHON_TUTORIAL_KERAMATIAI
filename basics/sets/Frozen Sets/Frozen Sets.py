"""
In Python, a frozen set is an immutable collection of unique elements, similar to a regular set but with the distinction that it cannot be modified after creation. Once created, the elements within a frozen set cannot be added, removed, or modified, making it a suitable choice when you need an immutable set.

You can create a frozen set in Python using the frozenset() function by passing an iterable (such as a list, tuple, or another set) containing the elements you want to include in the frozen set.

Example
In the following example, we are creating a frozen set of integers and then adding an element to it −
"""
my_frozen_set = frozenset([1, 2, 3])
print(my_frozen_set)
my_frozen_set.add(4)
"""
Following is the output of the above code −

frozenset({1, 2, 3})
Traceback (most recent call last):
  File "/home/cg/root/664b2732e125d/main.py", line 3, in <module>
    my_frozen_set.add(4)
AttributeError: 'frozenset' object has no attribute 'add'
"""