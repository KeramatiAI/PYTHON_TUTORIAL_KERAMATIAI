"""
Set comprehension in Python is a concise way to create sets using an iterable, similar to list comprehension but resulting in a set instead of a list. It allows you to generate sets by applying an expression to each item in an iterable while optionally filtering the items based on a condition.

We can join python sets using set comprehension by iterating over multiple sets and adding their elements to a new set.

Example
In this example, we are creating a new set "joined_set" using a set comprehension. By iterating over a list containing "set1" and "set2", and then iterating over each element "x" within each set "s", we merge all elements from both sets into "joined_set" −
"""
set1 = {1, 2, 3}
set2 = {3, 4, 5}

joined_set = {x for s in [set1, set2] for x in s}
print(joined_set)
"""
Output of the above code is as shown below −

{1, 2, 3, 4, 5}
"""