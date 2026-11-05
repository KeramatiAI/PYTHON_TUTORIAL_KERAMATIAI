"""
Add Dictionary Item Using the setdefault() Method
The setdefault() method in Python is used to get the value of a specified key in a dictionary. If the key does not exist, it inserts the key with a specified default value.

We can add dictionary items using the setdefault() method by specifying a key and a default value.

Example
In this example, we use the setdefault() to add the key-value pair "major": "Computer Science" to the "student" dictionary −
"""
# Initial dictionary
student = {"name": "Alice", "age": 21}
# Adding a new key-value pair
major = student.setdefault("major", "Computer Science")
print(student)
"""
Since the key "major" does not exist, it is added with the specified default value as shown in the output below −

{'name': 'Alice', 'age': 21, 'major': 'Computer Science'}
"""