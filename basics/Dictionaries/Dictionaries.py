"""
Dictionaries in Python
In Python, a dictionary is a built-in data type that stores data in key-value pairs. It is an insertion-ordered and mutable collection. Each key must be unique and hashable, and values can be accessed using their corresponding keys. Dictionaries are often used to store data that is related, such as information associated with a specific entity or object, where you can quickly retrieve a value based on its key.

Python's dictionary is an example of a mapping type. A mapping object 'maps' the value of one object to another. To establish mapping between a key and a value, the colon (:) symbol is put between the two.

Each key-value pair is separated by a comma and enclosed within curly braces {}. The key and value within each pair are separated by a colon (:), forming the structure key:value.
Given below are some examples of Python dictionary objects −

capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
Key Features of Dictionaries
Following are the key features of dictionaries −

Insertion-ordered − Dictionaries maintain the order in which items are inserted. This is guaranteed as a language feature starting from Python 3.7; earlier versions did not preserve insertion order. Note that items cannot be accessed by their position, only by their keys.

Mutable − You can change, add, or remove items after the dictionary has been created.

Key-based access − Dictionaries do not have numeric indexes. Instead, keys are used to access the associated values.

Unique Keys − Each key in a dictionary must be unique. If you try to assign a value to an existing key, the old value will be replaced by the new value.

Heterogeneous − Values in a dictionary can be of any data type. Keys can also be of different types, as long as each key is hashable.
"""