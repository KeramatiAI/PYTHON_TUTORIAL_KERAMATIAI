"""
Creating a Dictionary
You can create a dictionary in Python by placing a comma-separated sequence of key-value pairs within curly braces {}, with a colon : separating each key and its associated value. Alternatively, you can use the dict() function.

Example
The following example demonstrates how to create dictionaries using both curly braces and the dict() function −
"""
# Creating a dictionary using curly braces
sports_player = {
   "Name": "Sachin Tendulkar",
   "Age": 48,
   "Sport": "Cricket"
}
print ("Dictionary using curly braces:", sports_player)
# Creating a dictionary using the dict() function
student_info = dict(name="Alice", age=21, major="Computer Science")
print("Dictionary using dict():",student_info)
"""
The result produced is as shown below −

Dictionary using curly braces: {'Name': 'Sachin Tendulkar', 'Age': 48, 'Sport': 'Cricket'}
Dictionary using dict(): {'name': 'Alice', 'age': 21, 'major': 'Computer Science'}
"""