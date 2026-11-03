"""
A set comprehension in Python is a concise way to create sets by iterating over an iterable and optionally applying a condition. It is used to generate sets using a syntax similar to list comprehensions but results in a set, ensuring all elements are unique and unordered.

We can iterate using set comprehension by defining a set comprehension expression within curly braces {} and specifying the iteration and condition logic within the expression. Following is the syntax −

result_set = {expression for item in iterable if condition}
Where,

expression − It is an expression to evaluate for each item in the iterable.

item − It is a variable representing each element in the iterable.

iterable − It is a collection to iterate over (e.g., list, tuple, set).

condition − It is optional condition to filter elements included in the resulting set.

Example
In this example, we are using a set comprehension to generate a set containing squares of even numbers from the original list "numbers" −

"""

# Original list
numbers = [1, 2, 3, 4, 5]

# Set comprehension to create a set of squares of even numbers
squares_of_evens = {x**2 for x in numbers if x % 2 == 0}
# Print the resulting set
print(squares_of_evens)
"""
Output

We get the output as shown below −

{16, 4}
"""