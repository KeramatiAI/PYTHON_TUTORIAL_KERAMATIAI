"""
Example: Using the del Statement
You can use the del statement to remove a specific key-value pair from a dictionary. In this example, the del statement removes the key 'age' along with its associated value from the 'person' dictionary −
"""
# Initial dictionary
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# Removing the key-value pair associated with the key 'age'
del person['age']
print(person)
"""
Output of the above code is as shown below −

{'name': 'Alice', 'city': 'New York'}
"""