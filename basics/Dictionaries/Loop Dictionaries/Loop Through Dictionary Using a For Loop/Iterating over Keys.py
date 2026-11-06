"""
Iterating over Keys
In this approach, the loop iterates over the keys of the dictionary. Inside the loop, you can access the value corresponding to each key using dictionary indexing −
"""
student = {"name": "Alice", "age": 21, "major": "Computer Science"}
for key in student:
   print(key, student[key])
"""
It will produce the following output −

name Alice
age 21
major Computer Science
"""