"""
Remove Dictionary Items Using Dictionary Comprehension
Dictionary comprehension is a concise way to create dictionaries in Python. It follows the same syntax as list comprehension but generates dictionaries instead of lists. With dictionary comprehension, you can iterate over iterable objects (such as lists, tuples, or other dictionaries), apply an expression to each item, and construct key-value pairs based on the result of that expression.

We cannot directly remove dictionary items using dictionary comprehension. Dictionary comprehension is primarily used for creating new dictionaries based on some transformation or filtering of existing data, rather than for removing items from dictionaries.
If you need to remove items from a dictionary based on certain conditions, you would typically use other methods like del, pop(), or popitem(). These methods allow you to explicitly specify which items to remove from the dictionary.

Example
In this example, we remove items 'age' and 'major' from the 'student_info' dictionary based on a predefined list of keys to remove −
"""
# Creating a dictionary
student_info = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science"
}

# Removing items based on conditions
keys_to_remove = ["age", "major"]
for key in keys_to_remove:
    student_info.pop(key, None)

print(student_info)
"""
The output obtained is as shown below −

{'name': 'Alice'}
"""