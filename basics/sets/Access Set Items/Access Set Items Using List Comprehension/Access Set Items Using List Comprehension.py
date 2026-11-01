"""
List comprehension is an efficient way to create lists in Python. It allows you to generate a new list by applying an expression to each item in an iterable, optionally including a condition to filter elements.

We can access set items using list comprehension by converting the set into a list within the comprehension. This allows you to iterate over the set elements and perform operations on them, similar to using a for loop.

Example
In this example, we are using list comprehension to access set items by iterating over each element of "my_set" −
"""
my_set = {1, 2, 3, 4, 5}
# Accessing set items using list comprehension
accessed_items = [item for item in my_set]
print(accessed_items)
"""
We get the output as shown below −

[1, 2, 3, 4, 5]
"""