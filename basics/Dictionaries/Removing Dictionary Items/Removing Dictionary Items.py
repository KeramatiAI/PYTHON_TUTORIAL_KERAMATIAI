"""
Removing Dictionary Items
You can remove items using the del statement, the pop() method, or the popitem() method −
"""
student_info = {
   "name": "Alice",
   "age": 22,
   "major": "Computer Science",
   "graduation_year": 2023
}
# Removing an item using the del statement
del student_info["major"]

# Removing an item using the pop() method
graduation_year = student_info.pop("graduation_year")

print(student_info)
"""
Following is the output of the above code −

{'name': 'Alice', 'age': 22}
"""