"""
We can also remove set items using the pop() method by removing and returning an arbitrary element from the set. If the set is empty, the pop() method will raise a KeyError exception.

Example
In the example below, we are defining a set with elements "1" through "5" and removing an arbitrary element from it using the pop() method −
"""
# Defining a set
my_set = {1, 2, 3, 4, 5}

# removing and returning an arbitrary element from the set
removed_element = my_set.pop()

# Printing the removed element and the updated set
print("Removed Element:", removed_element)
print("Updated Set:", my_set)
"""
We get the output as shown below −

Removed Element: 1
Updated Set: {2, 3, 4, 5}
"""