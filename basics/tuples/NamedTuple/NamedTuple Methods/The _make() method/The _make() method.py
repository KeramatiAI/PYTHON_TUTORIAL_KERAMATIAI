"""
The _make() method is used to create a new instance of the namedtuple from an iterable (like a list or a tuple).

The following example demonstrates how to use the _make() method −
"""
from collections import namedtuple

# Define a namedtuple
Point = namedtuple('Point', ['x', 'y'])

# Create an instance
p = Point(10, 20)

# Create a new instance using _make()
p2 = Point._make([30, 40])

# Access fields
print("p2.x:", p2.x)
print("p2.y:", p2.y)
"""
The output of the above code will be −

p2.x: 30
p2.y: 40
"""