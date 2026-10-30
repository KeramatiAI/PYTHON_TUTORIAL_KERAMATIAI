from collections import namedtuple

# Define a namedtuple
Point = namedtuple('Point', ['x', 'y'])

# Create an instance
p = Point(10, 20)

# Access fields by keyname
print("Point-1:", p.x)
print("Point-2:", p.y)