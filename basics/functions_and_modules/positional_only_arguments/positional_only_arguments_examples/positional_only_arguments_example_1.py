"""
Positional Only Arguments
It is possible in Python to define a function in which one or more arguments can not accept their value with keywords. Such arguments are called positional-only arguments.

To make an argument positional-only, use the forward slash (/) symbol. All the arguments before this symbol will be treated as positional-only.

Python's built-in input() function is an example of positional-only arguments. The syntax of input function is −

input(prompt = "")
Prompt is an explanatory string for the benefit of the user. However, you cannot use the prompt keyword inside the parentheses.
"""
name = input(prompt="Enter your name ") # TypeError: input() takes no keyword arguments
"""
name = input (prompt="Enter your name ")
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: input() takes no keyword arguments
"""