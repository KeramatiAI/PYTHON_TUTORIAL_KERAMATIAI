"""
Default Values in Dataclass
You can also provide default values for the attributes in a dataclass. If a value is not provided during the creation of an instance, then the default value will be used. In the code below, we have provided a default value of 0.0 for the percent attribute.
"""
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    percent: float = 0.0  # Default value for percent

s1 = Student("Alice", 20)
s2 = Student("Bob", 22, 85.5)
print(s1)
print(s2)
"""
The output of the above code will be −

Student(name='Alice', age=20, percent=0.0)
Student(name='Bob', age=22, percent=85.5)
"""