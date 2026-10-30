"""
We already saw how to access the fields of a namedtuple using dot notation(i.e., using keyname). There are some other ways to access the fields as well −

Accessing by Indexing − You can access the fields using their index, just like a regular tuple.
Accessing by keyname − You can also access the fields using their key names, similar to a dictionary.
Accessing Using getattr() − You can use the getattr() function to access the fields by name.
Example: Accessing by Indexing
In this example, we will access the fields of the namedtuple using their index.
"""
from collections import namedtuple

# Define a namedtuple
Point = namedtuple('Point', ['x', 'y'])

# Create an instance
p = Point(10, 20)

# Access fields by indexing
print("Point-1", p[0])
print("Point-2", p[1])
"""
The output of the above code will be −

Point-1 10
Point-2 20
"""