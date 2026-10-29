"""
List comprehension is a concise way to create lists in Python. It is used to generate new lists by applying an expression to each item in an existing iterable, such as a list, tuple, or range. The syntax for list comprehension is −

new_list = [expression for item in iterable]
This creates a new list where expression is evaluated for each item in the iterable.

We can join a tuple using list comprehension by iterating over multiple tuples and appending their elements to a new tuple.
"""
# Two tuples to be joined
T1 = (36, 24, 3)
T2 = (84, 5, 81)
# Joining the tuples using list comprehension
joined_tuple = [item for subtuple in [T1, T2] for item in subtuple]
# Printing the joined tuple
print("Joined Tuple:", joined_tuple)