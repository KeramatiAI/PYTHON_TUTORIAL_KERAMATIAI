"""
Deleting a Dictionary from a Nested Dictionary
We can delete dictionaries from a nested dictionary by using the del keyword. This keyword allows us to remove a specific key-value pair from the nested dictionary.

Example
In the following example, we delete the nested dictionary for "Bob" from "students" dictionary using the del statement −
"""
# Define a nested dictionary
students = {
    "Alice": {"age": 21, "major": "Computer Science"},
    "Bob": {"age": 20, "major": "Engineering"},
    "Charlie": {"age": 22, "major": "Mathematics"}
}

# Delete the dictionary for Bob
del students["Bob"]

# Print the updated nested dictionary
print(students)
"""
We get the output as shown below −

{'Alice': {'age': 21, 'major': 'Computer Science'}, 'Charlie': {'age': 22, 'major': 'Mathematics'}}
"""