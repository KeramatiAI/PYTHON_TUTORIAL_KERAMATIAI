"""
Modifying Dictionary Items
You can modify the value associated with a specific key or add a new key-value pair −
"""
student_info = {
   "name": "Alice",
   "age": 21,
   "major": "Computer Science"
}
# Modifying an existing key-value pair
student_info["age"] = 22

# Adding a new key-value pair
student_info["graduation_year"] = 2023
print("The modified dictionary is:",student_info)
"""
Output of the above code is as follows −

The modified dictionary is: {'name': 'Alice', 'age': 22, 'major': 'Computer Science', 'graduation_year': 2023}
"""