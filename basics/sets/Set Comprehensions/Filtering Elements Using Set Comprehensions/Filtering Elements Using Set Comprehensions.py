"""
You can include conditional statements in set comprehensions to filter elements based on certain criteria. For instance, to create a set of even numbers from 1 to 10, you can use a set comprehension with an if condition as shown below −
"""
even_set = {x for x in range(1, 11) if x % 2 == 0}
print(even_set)

