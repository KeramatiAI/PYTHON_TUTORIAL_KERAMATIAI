"""
Add Dictionary Item Using the collections.defaultdict() Method
The collections.defaultdict() method in Python is a subclass of the built-in "dict" class that creates dictionaries with default values for keys that have not been set yet. It is part of the collections module in Python's standard library.

We can add dictionary items using the collections.defaultdict() method by specifying a default factory, which determines the default value for keys that have not been set yet. When accessing a missing key for the first time, the default factory is called to create a default value, and this value is inserted into the dictionary.

Example
In this example, we are initializing instances of defaultdict with different default factories: int to initialize missing keys with 0, list to initialize missing keys with an empty list, and a custom function default_value to initialize missing keys with the return value of the function −
"""
from collections import defaultdict
# Using int as the default factory to initialize missing keys with 0
d = defaultdict(int)
# Incrementing the value for key 'a'
d["a"] += 1
print(d)

# Using list as the default factory to initialize missing keys with an empty list
d = defaultdict(list)
# Appending to the list for key 'b'
d["b"].append(1)
print(d)

# Using a custom function as the default factory
def default_value():
    return "N/A"

d = defaultdict(default_value)
print(d["c"])
"""
The output obtained is as follows −

defaultdict(<class 'int'>, {'a': 1})
defaultdict(<class 'list'>, {'b': [1]})
N/A
"""