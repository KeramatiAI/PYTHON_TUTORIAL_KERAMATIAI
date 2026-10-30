"""
The _replace() method is used to create a new instance of the namedtuple with one or more fields replaced with new values. It takes keyword arguments where the keys are the field names and the values are the new values to be assigned.

The following example demonstrates how to use the _replace() method −
"""
from collections import namedtuple

# Define a namedtuple
Point = namedtuple('Point', ['x', 'y'])

# Create an instance
p = Point(10, 20)

# Replace a field value
p2 = p._replace(x=30)

# Access fields
print("p2.x:", p2.x)
print("p2.y:", p2.y)
"""
The output of the above code will be −

p2.x: 30
p2.y: 20
"""