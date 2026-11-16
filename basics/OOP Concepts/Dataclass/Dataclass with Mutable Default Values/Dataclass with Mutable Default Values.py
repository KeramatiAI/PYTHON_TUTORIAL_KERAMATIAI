"""
Dataclass with Mutable Default Values
Mutable default values refers to default values that can be modified after the instance is created, such as lists or dictionaries. When using mutable default values in a dataclass, it is recommended to use the field() function from the dataclasses module with the default_factory parameter. Because if you use a mutable object as a default value directly, it will be shared across all instances of the dataclass. This can lead security issues and unexpected behavior.

In the code below, we have defined a dataclass named Course with a mutable default value for the students attribute.
"""
from dataclasses import dataclass, field
from typing import List
@dataclass
class Course:
    name: str
    students: List[str] = field(default_factory=list)  # Mutable default value

course1 = Course("Math")
course2 = Course("Science", ["Alice", "Bob"])
course1.students.append("Charlie")
print(course1)
print(course2)
"""
The output of the above code will be −

Course(name='Math', students=['Charlie'])
Course(name='Science', students=['Alice', 'Bob'])
Explantion: If you used students: List[str] = [] directly, all the instances of Course will get the same list, because default values are evaluated only once, i.e., during creation of class. By using field(default_factory=list), Python ensures that every Course instance gets its own separate list and avoids security vulnerabilities.
"""