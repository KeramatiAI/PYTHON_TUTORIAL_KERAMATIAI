"""
Conditional Dictionary Modification
Conditional modification in a Python dictionary refers to changing the value associated with a key only if a certain condition is met.

You can use an if statement to check whether a certain condition is true before modifying the value associated with a key.

Example
In this example, we conditionally modify the value associated with the key 'age' to '26' if the current value is '25' in the 'persons' dictionary −
"""
# Initial dictionary
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# Conditionally modifying the value associated with 'age'
if person['age'] == 25:
   person['age'] = 26
print(person)
"""
The output obtained is as shown below −

{'name': 'Alice', 'age': 26, 'city': 'New York'}
"""