"""
Updating Multiple Dictionary Values
If you need to update multiple values in a dictionary at once, you can use the update() method. This method is used to update a dictionary with elements from another dictionary or an iterable of key-value pairs.

The update() method adds the key-value pairs from the provided dictionary or iterable to the original dictionary, overwriting any existing keys with the new values if they already exist in the original dictionary.

Example
In the example below, we are using the update() method to modify the values associated with the keys 'age' and 'city' in the 'persons' dictionary −
"""
# Initial dictionary
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# Updating multiple values
person.update({'age': 26, 'city': 'Los Angeles'})
print(person)
"""
We get the output as shown below −

{'name': 'Alice', 'age': 26, 'city': 'Los Angeles'}
"""