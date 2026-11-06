"""
Loop Through Dictionary Using dict.values() Method
The dict.values() method in Python is used to return a view object that displays a list of values in the dictionary. This view object provides a dynamic view of the dictionary's values, allowing you to access and iterate over them.

We can loop through dictionaries using the dict.values() method by iterating over the values returned by this method. This allows us to access and iterate over the values of the dictionary.

Example
In the following example, the values() method is called on the "student" dictionary, returning a view object containing the values −
"""
student = {"name": "Alice", "age": 21, "major": "Computer Science"}

# Looping through values
for value in student.values():
   print(value)
"""
Output of the above code is as shown below −

Alice
21
Computer Science
"""