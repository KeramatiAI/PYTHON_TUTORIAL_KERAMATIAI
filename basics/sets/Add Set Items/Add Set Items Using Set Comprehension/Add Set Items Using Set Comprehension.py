"""
In Python, set comprehension is a way to create sets using a single line of code. It allows you to generate a new set by applying an expression to each item in an iterable (such as a list, tuple, or range), optionally including a condition to filter elements.

We can add set items using set comprehension by iterating over an iterable, applying an expression to each element, and enclosing the comprehension expression within curly braces {} to generate a new set containing the results of the expression applied to each element.

Example
In the following example, we are defining a list of integers and then using set comprehension to generate a set containing the squares of those integers −
"""
# Defining a list containing integers
numbers = [1, 2, 3, 4, 5]
# Creating a set containing squares of numbers using set comprehension
squares_set = {num ** 2 for num in numbers}
# Printing the set containing squares of numbers
print("Squares Set:", squares_set)
"""
Following is the output of the above code −

Squares Set: {1, 4, 9, 16, 25}
"""