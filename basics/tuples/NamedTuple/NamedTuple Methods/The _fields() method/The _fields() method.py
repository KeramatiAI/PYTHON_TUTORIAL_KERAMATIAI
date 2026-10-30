"""
The_fields() method is used to access the field names of the namedtuple. It doesn't need any arguments and returns a tuple of the field names.

The following example demonstrates how to use the _fields() method −
"""
from collections import namedtuple

# Define a namedtuple
Point = namedtuple('Point', ['x', 'y'])

# Create an instance
p = Point(10, 20)

# Access fields using _fields()
print("Fields of p:", p._fields)
"""
The output of the above code will be −

Fields of p: ('x', 'y')
"""