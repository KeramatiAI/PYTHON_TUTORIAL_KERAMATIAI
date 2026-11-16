"""
Creating a Dataclass
In the code below, you can see that we have defined a simple dataclass named Student with three attributes: name, age, and percent. Even though we are not using constructor or other special methods, we can still create instances of the Student class and use its attributes. This is because the dataclass decorator automatically generates these methods for us.
"""
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    percent: float

s1 = Student("Alice", 20, 90.0)
s2 = Student("Bob", 22, 85.5)

print(s1)
print(s1 == s2)
"""
The output of the above code will be −

Student(name='Alice', age=20, percent=90.0)
False
"""