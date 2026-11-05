"""
Example: Using the popitem() Method
You can use the popitem() method as well to remove the last key-value pair from a dictionary and return it as a tuple.

Now, the popitem() method removes the last key-value pair from the 'person' dictionary and returns it as a tuple −
"""
# Initial dictionary
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# Removing the last key-value pair
removed_item = person.popitem()

print(person)
print("Removed item:", removed_item)
"""
We get the output as shown below −

{'name': 'Alice', 'age': 25}
Removed item: ('city', 'New York')
"""