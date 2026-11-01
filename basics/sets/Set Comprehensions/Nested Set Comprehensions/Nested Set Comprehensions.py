"""
Set comprehensions also support nested loops, allowing you to create sets from nested iterables. This can be useful for generating combinations or permutations of elements.
"""
nested_set = {(x, y) for x in range(1, 3) for y in range(1, 3)}
print(nested_set)
"""
Output of the above code is as shown below −

{(1, 1), (1, 2), (2, 1), (2, 2)}
"""