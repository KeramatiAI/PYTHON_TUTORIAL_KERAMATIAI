"""
Immuatable/Frozen Dataclasses
An immutable or frozen dataclass indicates that the instances of the dataclass cannot be modified after they are created. This can be achieved by setting the frozen parameter to True in the @dataclass decorator. When a dataclass is frozen, any attempt to modify its attributes will create a FrozenInstanceError.

The frozen dataclasses are often used to secure applications by preventing unauthorized access or modification of sensitive data. In the code below, we have defined a frozen dataclass named Point with two attributes: x and y. We will catch the FrozenInstanceError when trying to modify the x attribute.
"""
from dataclasses import dataclass, FrozenInstanceError
@dataclass(frozen=True)
class Point:
    x: int
    y: int
p = Point(1, 2)
print(p)

try:
    p.x = 10  # This will raise an error
except FrozenInstanceError as e:
    print(e)
"""
The output of the above code will be −

Point(x=1, y=2)
cannot assign to field 'x'
"""