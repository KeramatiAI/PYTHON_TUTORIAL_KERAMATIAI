"""
Using a Loop
With this method, an empty outer dictionary is initialized, and then populated with dictionaries as values using a loop to define nested dictionaries −
"""
# Define an empty outer dictionary
nested_dict = {}

# Add key-value pairs to the outer dictionary
outer_keys = ["outer_key1", "outer_key2"]
for key in outer_keys:
   nested_dict[key] = {"inner_key1": "value1", "inner_key2": "value2"}
print(nested_dict)
