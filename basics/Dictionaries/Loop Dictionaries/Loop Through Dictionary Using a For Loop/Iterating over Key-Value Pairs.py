"""
Iterating over Key-Value Pairs
In this approach, the loop iterates over the key-value pairs using the items() method of the dictionary. Each iteration provides both the key and its corresponding value −
"""
student = {"name": "Alice", "age": 21, "major": "Computer Science"}
for key, value in student.items():
   print(key, value)
"""
We get the output as shown below −

name Alice
age 21
major Computer Science
"""