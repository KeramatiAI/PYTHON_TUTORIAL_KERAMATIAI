"""
Deep Copy
A deep copy creates a new dictionary and recursively copies all objects found in the original dictionary. This means that not only the dictionary itself but also all objects it contains (including nested dictionaries, lists, etc.) are copied. As a result, changes made to the deep copy do not affect the original dictionary and vice versa.

We can achieve this using the deepcopy() function in the copy module.

Example
We can see in the example below that the "age" value in the deep copy is changed, the "skills" list in the deep copy is modified (an item is appended) and the "education" dictionary in the deep copy is modified, all without affecting the original −
"""
import copy

original_dict = {
    "name": "Alice",
    "age": 25,
    "skills": ["Python", "Data Science"],
    "education": {
      "degree": "Bachelor's",
      "field": "Computer Science"
   }
}

# Creating a deep copy
deep_copy = copy.deepcopy(original_dict)

# Modifying the deep copy
deep_copy["age"] = 26
deep_copy["skills"].append("Machine Learning")
deep_copy["education"]["degree"] = "Master's"

# Retrieving both dictionaries
print("Original dictionary:", original_dict)
print("Deep copy:", deep_copy)
"""
This will produce the following output -- MOHTASHIM −

Original dictionary: {'name': 'Alice', 'age': 25, 'skills': ['Python', 'Data Science'], 'education': {'degree': "Bachelor's", 'field': 'Computer Science'}}
Deep copy: {'name': 'Alice', 'age': 26, 'skills': ['Python', 'Data Science', 'Machine Learning'], 'education': {'degree': "Master's", 'field': 'Computer Science'}}
"""