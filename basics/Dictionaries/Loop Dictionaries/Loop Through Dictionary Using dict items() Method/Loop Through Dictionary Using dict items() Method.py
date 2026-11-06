"""
Loop Through Dictionary Using dict.items() Method
The dict.items() method in Python is used to return a view object that displays a list of key-value pairs in the dictionary. This view object provides a dynamic view of the dictionary's items, allowing you to access both the keys and their corresponding values.

We can loop through dictionaries using the dict.items() method by iterating over the key-value pairs returned by this method.

Example
In this example, the items() method is called on the "student" dictionary, returning a view object containing the key-value pairs. The for loop iterates over each pair, assigning the key to the variable "key" and the corresponding value to the variable "value" −
"""
student = {"name": "Alice", "age": 21, "major": "Computer Science"}

# Looping through key-value pairs
for key, value in student.items():
   print(key, value)
"""
The output produced is as shown below −

name Alice
age 21
major Computer Science
"""