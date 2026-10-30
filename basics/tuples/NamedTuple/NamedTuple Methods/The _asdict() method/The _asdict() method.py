"""
The _asdict() method is used to convert the namedtuple into a regular dictionary. This function returns the OrderedDict() as constructed from the mapped values of namedtuple().

The following example demonstrates how to use the _asdict() method −
"""
from collections import namedtuple

# Define a namedtuple
Point = namedtuple('Point', ['x', 'y'])

# Create an instance
p = Point(10, 20)

# Convert to dictionary
d = p._asdict()
print(d)
"""
The output of the above code will be −

{'x': 10, 'y': 20}
"""