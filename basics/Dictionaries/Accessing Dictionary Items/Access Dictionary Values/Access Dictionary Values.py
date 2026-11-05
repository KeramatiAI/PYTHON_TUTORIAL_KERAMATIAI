"""
Access Dictionary Values
In a dictionary, values are the data associated with each unique key. They represent the actual information stored in the dictionary and can be of any data type, such as strings, integers, lists, other dictionaries, and more. Each key in a dictionary maps to a specific value, forming a key-value pair.

We can access dictionary values in Python using −

Square Brackets ([]) − By providing the key inside the brackets.

The get() Method − By calling the method with the key as an argument, optionally providing a default value.

The values() Method − which returns a view object containing all the values in the dictionary

Example 1
In this example, we are directly accessing associated with the key "name" and "age" using the sqaure brackets −
"""
# Creating a dictionary with student information
student_info = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science"
}
# Accessing dictionary values using square brackets
name = student_info["name"]
age = student_info["age"]
print("Name:", name)
print("Age:", age)
"""
Output of the above code is as follows −

Name: Alice
Age: 21
"""