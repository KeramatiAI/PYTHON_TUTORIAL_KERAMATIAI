"""
Syntax of Python List Comprehension
The basic syntax of list comprehension is −

new_list = [expression for item in iterable if condition]
Where,

expression is the operation or transformation to apply to each item in the iterable.
item is the variable representing each element in the iterable.
iterable is the sequence of elements to iterate over.
condition (optional) is an expression that filters elements based on a specified condition.
"""
string = "hello world"
uppercase_letters = [char.upper() for char in string if char.isalpha()]
print(uppercase_letters)
