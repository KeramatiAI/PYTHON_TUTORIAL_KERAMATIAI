"""
Accessing Dictionary Items
You can access the value associated with a specific key using square brackets [] or the get() method −
"""
student_info = {
   "name": "Alice",
   "age": 21,
   "major": "Computer Science"
}
# Accessing values using square brackets
name = student_info["name"]
print("Name:",name)

# Accessing values using the get() method
age = student_info.get("age")
print("Age:",age)
"""
The result obtained is as follows −

Name: Alice
Age: 21
"""