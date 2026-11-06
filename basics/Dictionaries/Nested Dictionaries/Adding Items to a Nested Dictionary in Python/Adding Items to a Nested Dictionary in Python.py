"""
Adding Items to a Nested Dictionary in Python
Once a nested dictionary is created, we can add items to it by accessing the specific nested dictionary using its key and then assigning a new key-value pair to it.

Example
In the following example, we are defining a nested dictionary "students" where each key represents a student's name and its value is another dictionary containing details about the student.

Then, we add a new key-value pair to Alice's nested dictionary and add a new nested dictionary for a new student, Charlie −
"""
# Initial nested dictionary
students = {
    "Alice": {"age": 21, "major": "Computer Science"},
    "Bob": {"age": 20, "major": "Engineering"}
}

# Adding a new key-value pair to Alice's nested dictionary
students["Alice"]["GPA"] = 3.8

# Adding a new nested dictionary for a new student
students["Charlie"] = {"age": 22, "major": "Mathematics"}

print(students)
"""
It will produce the following output −

{'Alice': {'age': 21, 'major': 'Computer Science', 'GPA': 3.8}, 'Bob': {'age': 20, 'major': 'Engineering'}, 'Charlie': {'age': 22, 'major': 'Mathematics'}}
"""