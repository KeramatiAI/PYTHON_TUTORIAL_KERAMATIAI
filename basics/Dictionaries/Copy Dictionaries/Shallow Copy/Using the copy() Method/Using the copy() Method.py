"""
Using the copy() Method
In the following example, we can see that changing the "age" in the shallow copy does not affect the original.

However, modifying the list in the shallow copy also affects the original because the list is a mutable object and only a reference is copied.
"""
original_dict = {"name": "Alice", "age": 25, "skills": ["Python", "Data Science"]}
shallow_copy = original_dict.copy()

# Modifying the shallow copy
shallow_copy["age"] = 26
shallow_copy["skills"].append("Machine Learning")

print("Original dictionary:", original_dict)
print("Shallow copy:", shallow_copy)
"""
Following is the output of the above code −

Original dictionary: {'name': 'Alice', 'age': 25, 'skills': ['Python', 'Data Science', 'Machine Learning']}
Shallow copy: {'name': 'Alice', 'age': 26, 'skills': ['Python', 'Data Science', 'Machine Learning']}
"""