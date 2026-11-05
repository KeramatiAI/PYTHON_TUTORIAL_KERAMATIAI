"""
Access Dictionary Items Using get() Method
The get() method in Python's dict class is used to retrieve the value associated with a specified key. If the key is not found in the dictionary, it returns a default value (usually None) instead of raising a KeyError.

We can access dictionary items using the get() method by specifying the key as an argument. If the key exists in the dictionary, the method returns the associated value; otherwise, it returns a default value, which is often None unless specified otherwise.

Syntax
Following is the syntax of the get() method in Python −

Val = dict.get("key")
where, key is an immutable object used as key in the dictionary object.

Example 1
In the example below, we are defining a dictionary named "capitals" where each key-value pair maps a state to its capital city. Then, we use the get() method to retrieve the capital cities of "Gujarat" and "Karnataka" −
"""
capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
print ("Capital of Gujarat is: ", capitals.get('Gujarat'))
print ("Capital of Karnataka is: ", capitals.get('Karnataka'))
"""
We get the output as shown below −

Capital of Gujarat is: Gandhinagar
Capital of Karnataka is: Bengaluru
"""