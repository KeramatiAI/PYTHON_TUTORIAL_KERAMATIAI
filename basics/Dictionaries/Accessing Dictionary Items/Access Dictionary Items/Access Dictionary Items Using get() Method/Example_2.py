"""
Example 2
Unlike the "[]" operator, the get() method doesn't raise error if the key is not found; it return None −
"""
capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
print ("Capital of Haryana is : ", capitals.get('Haryana'))
"""
It will produce the following output −

Capital of Haryana is : None
"""