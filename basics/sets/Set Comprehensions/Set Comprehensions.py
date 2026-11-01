"""
Set comprehensions in Python is a concise way to create sets based on iterable objects, similar to list comprehensions. It is used to generate sets by applying an expression to each item in an iterable.

Set comprehensions are useful when you need to create a set from the result of applying some operation or filtering elements from another iterable.

Syntax
The syntax for set comprehensions is similar to list comprehensions, but instead of square brackets [ ], you use curly braces { } to denote a set −

set_variable = {expression for item in iterable if condition}

"""
squared_set = {x**2 for x in range(1, 6)}
print(squared_set)