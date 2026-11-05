"""
Example: Using the pop() Method
You can also use the pop() method to remove a specific key-value pair from a dictionary and return the value associated with the removed key.

In here, the pop() method removes the key 'age' along with its associated value from the 'person' dictionary −
"""
# Initial dictionary
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# Removing the key-value pair associated with the key 'age'
removed_age = person.pop('age')

print(person)
print("Removed age:", removed_age)
"""
It will produce the following output −

{'name': 'Alice', 'city': 'New York'}
Removed age: 25
"""