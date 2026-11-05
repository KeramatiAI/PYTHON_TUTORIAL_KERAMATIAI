"""
Example 2
In here, we use the get() method to retrieve the value associated with the key "major" and provide a default value of "2023" for the key "graduation_year" −
"""
# Creating a dictionary with student information
student_info = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science"
}
# Accessing dictionary values using the get() method
major = student_info.get("major")
# Default value provided if key is not found
grad_year = student_info.get("graduation_year", "2023")

print("Major:", major)
print("Graduation Year:", grad_year)
"""
We get the result as follows −

Major: Computer Science
Graduation Year: 2023
"""