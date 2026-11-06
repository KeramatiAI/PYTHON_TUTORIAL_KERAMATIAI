"""
Using the dict() Method
Similar to the copy() method, the dict() method creates a shallow copy as shown in the example below −
"""
original_dict = {"name": "Bob", "age": 30, "skills": ["Java", "C++"]}
shallow_copy = dict(original_dict)

# Modifying the shallow copy
shallow_copy["age"] = 31
shallow_copy["skills"].append("C#")

print("Original dictionary:", original_dict)
print("Shallow copy:", shallow_copy)
"""
Output of the above code is as follows −

Original dictionary: {'name': 'Bob', 'age': 30, 'skills': ['Java', 'C++', 'C#']}
Shallow copy: {'name': 'Bob', 'age': 31, 'skills': ['Java', 'C++', 'C#']}
"""