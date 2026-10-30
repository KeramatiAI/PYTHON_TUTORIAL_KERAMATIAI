"""
To create a namedtuple, you need to import the namedtuple function from the collections module. Then, you can define a namedtuple by specifying its name and field names.

The following example shows how to create a namedtuple called Point with fields x and y −
"""
from collections import namedtuple

# Define a namedtuple
Vertex = namedtuple('Vertex', ['x', 'y'])

# Create an instance
v = Vertex(10, 20)

# Access fields
print("Vertex-1:", v.x)
print("Vertex-2:", v.y)
"""
The output of the above code will be −

Vertex-1: 10
Vertex-2: 20
"""