"""
Iterating Through a Nested Dictionary in Python
Iterating through a nested dictionary refers to looping through the keys and values at each level of the dictionary. This allows you to access and manipulate items within the nested structure.

We can iterate through a nested dictionary by using nested loops. The outer loop iterates over the keys and values of the main dictionary, while the inner loop iterates over the keys and values of the nested dictionaries.

Example
In this example, we are iterating through the "students" dictionary, retrieving each student's name and their corresponding details by iterating through the nested dictionaries −
"""
# Defining a nested dictionary
students = {
    "Alice": {"age": 21, "major": "Computer Science"},
    "Bob": {"age": 20, "major": "Engineering"},
    "Charlie": {"age": 22, "major": "Mathematics"}
}

# Iterating through the Nested Dictionary:
for student, details in students.items():
   print(f"Student: {student}")
   for key, value in details.items():
      print(f"  {key}: {value}")
"""
The output obtained is as shown below −

Student: Alice
  age: 21
major: Computer Science
Student: Bob
  age: 20
  major: Engineering
Student: Charlie
  age: 22
  major: Mathematics
"""