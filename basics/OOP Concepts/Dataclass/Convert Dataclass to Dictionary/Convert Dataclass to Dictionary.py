"""
Convert Dataclass to Dictionary
You can convert a dataclass instance to a dictionary using the asdict() function from the dataclasses module. This function recursively converts the dataclass and its fields into a dictionary. This is useful when you want to serialize the dataclass instance or work with its data in a dictionary format.
"""
from dataclasses import dataclass, asdict
from typing import List

@dataclass
class Student:
    name: str
    age: int
    grades: List[float]

student = Student("Alice", 20, [88.5, 92.0, 79.5])
student_dict = asdict(student)
print(student_dict)
"""
The output of the above code will be −

{'name': 'Alice', 'age': 20, 'grades': [88.5, 92.0, 79.5]}
"""