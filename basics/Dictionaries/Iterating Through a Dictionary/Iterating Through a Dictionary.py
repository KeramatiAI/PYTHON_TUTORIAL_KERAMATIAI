"""
Iterating Through a Dictionary
You can iterate through the keys, values, or key-value pairs in a dictionary using loops −
"""
student_info = {
   "name": "Alice",
   "age": 22,
   "major": "Computer Science",
   "graduation_year": 2023
}
# Iterating through keys
for key in student_info:
   print("Keys:",key, student_info[key])

# Iterating through values
for value in student_info.values():
   print("Values:",value)

# Iterating through key-value pairs
for key, value in student_info.items():
   print("Key:Value:",key, value)
"""
After executing the above code, we get the following output −

Keys: name Alice
Keys: age 22
Keys: major Computer Science
Keys: graduation_year 2023
Values: Alice
Values: 22
Values: Computer Science
Values: 2023
Key:Value: name Alice
Key:Value: age 22
Key:Value: major Computer Science
Key:Value: graduation_year 2023
"""