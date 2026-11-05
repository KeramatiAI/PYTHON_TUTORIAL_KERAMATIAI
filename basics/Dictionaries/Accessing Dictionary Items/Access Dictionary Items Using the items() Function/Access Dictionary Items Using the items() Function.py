"""
Access Dictionary Items Using the items() Function
The items() function in Python is used to return a view object that displays a list of a dictionary's key-value tuple pairs.

This view object can be used to iterate over the dictionary's keys and values simultaneously, making it easy to access both the keys and the values in a single loop.

Example
In the following example, we are using the items() function to retrieve all the key-value pairs from the dictionary "student_info" −
"""
# Creating a dictionary with student information
student_info = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science"
}

# Using the items() method to get key-value pairs
all_items = student_info.items()
print("Items:", all_items)
# Iterating through the key-value pairs
print("Iterating through key-value pairs:")
for key, value in all_items:
    print(f"{key}: {value}")
"""
Following is the output of the above code −

Items: dict_items([('name', 'Alice'), ('age', 21), ('major', 'Computer Science')])
Iterating through key-value pairs:
name: Alice
age: 21
major: Computer Science
"""