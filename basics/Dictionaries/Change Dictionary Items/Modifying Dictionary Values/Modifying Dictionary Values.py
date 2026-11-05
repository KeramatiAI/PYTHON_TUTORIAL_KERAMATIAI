"""
Modifying Dictionary Values
Modifying values in a Python dictionary refers to changing the value associated with an existing key. To achieve this, you can directly assign a new value to that key.

Example
In the following example, we are defining a dictionary named "person" with keys 'name', 'age', and 'city' and their corresponding values. Then, we modify the value associated with the key 'age' to 26 −
"""
# Initial dictionary
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# Modifying the value associated with the key 'age'
person['age'] = 26
print(person)
"""
It will produce the following output −

{'name': 'Alice', 'age': 26, 'city': 'New York'}
"""