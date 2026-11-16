"""
Setting Up Post-Initialization
The post-Initialization refer to the additional initialization logic that can be added to a dataclass after the automatic __init__() method has been called. This can be done by defining a special method named __post_init__() in the dataclass. The __post_init__() method is called automatically after the instance is created and all the attributes have been initialized.

In the code below, we have defined a dataclass named Rectangle with default value for the area as 0.0. The area is then calculated in the __post_init__() method based on the recived width and height values.
"""
from dataclasses import dataclass
@dataclass
class Rectangle:
    width: float
    height: float
    area: float = 0.0  # This will be calculated in __post_init__

    def __post_init__(self):
        self.area = self.width * self.height  # Calculate area after initialization
r = Rectangle(5.0, 10.0)
print(r)
print(f"Area of the rectangle: {r.area}")
"""
The output of the above code will be −

Rectangle(width=5.0, height=10.0, area=50.0)
Area of the rectangle: 50.0
"""