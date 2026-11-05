"""
Access Dictionary Keys
In a dictionary, keys are the unique identifiers associated with each value. They act as labels or indices that allow you to access and retrieve the corresponding value. Keys are immutable, meaning they cannot be changed once they are assigned. They must be of an immutable data type, such as strings, numbers, or tuples.

We can access dictionary keys in Python using the keys() method, which returns a view object containing all the keys in the dictionary.

Example
In this example, we are retrieving all the keys from the dictionary "student_info" using the keys() method −
"""
# Creating a dictionary with keys and values
student_info = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science"
}
# Accessing all keys using the keys() method
all_keys = student_info.keys()
print("Keys:", all_keys)
"""
Following is the output of the above code −

Keys: dict_keys(['name', 'age', 'major'])
"""