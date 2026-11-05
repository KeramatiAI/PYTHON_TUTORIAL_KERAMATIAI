"""
Access Dictionary Items Using Square Brackets []
In Python, the square brackets [] are used for creating lists, accessing elements from a list or other iterable objects (like strings, tuples, or dictionaries), and for list comprehension.

We can access dictionary items using square brackets by providing the key inside the brackets. This retrieves the value associated with the specified key.

Example 1
In the following example, we are defining a dictionary named "capitals" where each key represents a state and its corresponding value represents the capital city.

Then, we access and retrieve the capital cities of Gujarat and Karnataka using their respective keys 'Gujarat' and 'Karnataka' from the dictionary −
"""
capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
print ("Capital of Gujarat is : ", capitals['Gujarat'])
print ("Capital of Karnataka is : ", capitals['Karnataka'])
"""
It will produce the following output −

Capital of Gujarat is: Gandhinagar
Capital of Karnataka is: Bengaluru
"""