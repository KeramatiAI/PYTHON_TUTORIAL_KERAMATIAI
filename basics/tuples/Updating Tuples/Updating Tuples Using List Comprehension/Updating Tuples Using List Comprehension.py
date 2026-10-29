"""
List comprehension in Python is a concise way to create lists. It allows you to generate new lists by applying an expression to each item in an existing iterable, such as a list, tuple, or string, optionally including a condition to filter elements.

Since tuples are immutable, updating a tuple involves converting it to a list, making the desired changes using list comprehension, and then converting it back to a tuple.

Example
In the example below, we are updating a tuple by first converting it to a list and using list comprehension to add 100 to each element. We then convert the list back to a tuple to get the updated tuple −

"""
# Original tuple
T1 = (10, 20, 30, 40)
# Converting the tuple to a list
list_T1 = list(T1)
# Using list comprehension
updated_list = [item + 100 for item in list_T1]
# Converting the updated list back to a tuple
updated_tuple = tuple(updated_list)
# Printing the updated tuple
print("Original Tuple:", T1)
print("Updated Tuple:", updated_tuple)