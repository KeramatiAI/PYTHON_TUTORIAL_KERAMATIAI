"""
Example 3
The get() method accepts an optional string argument. If it is given, and if the key is not found, this string becomes the return value −
"""
capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
print ("Capital of Haryana is : ", capitals.get('Haryana', 'Not found'))
"""
After executing the above code, we get the following output −

Capital of Haryana is: Not found
"""