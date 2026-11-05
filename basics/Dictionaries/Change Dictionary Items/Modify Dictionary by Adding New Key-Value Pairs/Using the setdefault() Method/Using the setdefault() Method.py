"""
Example: Using the setdefault() Method
You can use the setdefault() method to add a new key-value pair to a dictionary if the key does not already exist.

In this example, the setdefault() method adds the new key 'city' with the value 'New York' to the 'person' dictionary only if the key 'city' does not already exist −
"""
# Initial dictionary
person = {'name': 'Alice', 'age': 25}
# Adding a new key-value pair 'city': 'New York'
person.setdefault('city', 'New York')
print(person)
"""
Following is the output of the above code −

{'name': 'Alice', 'age': 25, 'city': 'New York'}
"""