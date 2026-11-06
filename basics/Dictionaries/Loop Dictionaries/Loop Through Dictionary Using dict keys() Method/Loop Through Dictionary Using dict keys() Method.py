"""
Loop Through Dictionary Using dict.keys() Method
The dict.keys() method in Python is used to return a view object that displays a list of keys in the dictionary. This view object provides a dynamic view of the dictionary's keys, allowing you to access and iterate over them.

We can loop through dictionaries using the dict.keys() method by iterating over the keys returned by this method. This allows us to access and iterate over the keys of the dictionary.

Example
In the example below, the keys() method is called on the "student" dictionary, returning a view object containing the keys. The for loop iterates over each key in the view object, allowing you to perform operations based on the keys of the dictionary during each iteration −
"""
student = {"name": "Alice", "age": 21, "major": "Computer Science"}

# Looping through keys
for key in student.keys():
   print(key)
"""
Following is the output of the above code −

name
age
major
"""